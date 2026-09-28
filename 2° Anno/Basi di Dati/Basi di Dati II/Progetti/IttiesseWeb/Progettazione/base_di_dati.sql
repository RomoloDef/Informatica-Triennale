CREATE DOMAIN Codice varchar
        CHECK (value ~ '^[A-Z0-9]{16}$');

CREATE DOMAIN Mail varchar 
        CHECK(value ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

CREATE DOMAIN IVA varchar 
        CHECK (value ~ '^[0-9]{11}$');

CREATE DOMAIN IntegerGZ AS Integer
        CHECK (value IS NOT NULL and VALUE > 0);

CREATE TYPE Periodo AS (
    da timestamp,
    a timestamp
);

CREATE TYPE TipoEsame AS ENUM ('Esame', 'EsameStato');

CREATE DOMAIN Votazione AS Integer 
     	CHECK (value IS NOT NULL and VALUE >= 0 AND VALUE <= 10);

CREATE TABLE Azienda(
	ragione_sociale varchar NOT NULL,
	partita_iva IVA NOT NULL,
	primary key (ragione_sociale)
);

CREATE TABLE Corso(
	nome varchar NOT NULL,
	durata interval NOT NULL,
	primary key(durata),
	CHECK (durata = interval '2 years')
);

CREATE TABLE Tirocinio(
	id serial NOT NULL,
	data_inizio timestamp NOT NULL,
	primary key (id)
);

CREATE TABLE Persona (
	nome varchar NOT NULL,
	cognome varchar NOT NULL,
	codice_fiscale Codice NOT NULL,
	primary key (codice_fiscale)
);

CREATE TABLE Docente (
	email Mail NOT NULL,
	persona Codice NOT NULL,
	primary key (persona),
	foreign key (persona) references Persona(codice_fiscale)
);

CREATE TABLE Studente (
	nascita timestamp NOT NULL,
	persona Codice NOT NULL,
	tirocinio_effettuato serial NOT NULL,
	primary key (persona),
	foreign key (persona) references Persona(codice_fiscale),
	foreign key (tirocinio_effettuato) references Tirocinio(id)
);

CREATE TABLE Iscrizione(
	id serial NOT NULL,
	istante_iscrizione timestamp NOT NULL,
	primary key (id)
);

CREATE TABLE stu_isc (
	studente Codice NOT NULL,
	iscrizione serial NOT NULL,
	primary key (studente, iscrizione),
	foreign key (studente) references Studente(persona),
	foreign key (iscrizione) references Iscrizione(id)
);

CREATE TABLE Edizione(
	anno integer NOT NULL,
	crediti_per_esame IntegerGZ NOT NULL,
	crediti_per_tirocinio IntegerGZ NOT NULL,
	iscrizione serial UNIQUE NOT NULL,
	corso interval NOT NULL,
	primary key (anno),
	foreign key (iscrizione) references Iscrizione(id),
	foreign key (corso) references Corso(durata)
);

CREATE TABLE Blocco(
	id serial NOT NULL,
	crediti_ottenuti IntegerGZ NOT NULL,
	primary key (id)
);

CREATE TABLE Partecipazione(
	id serial NOT NULL,
	istante_partecipazione timestamp NOT NULL,
	primary key (id)
);

CREATE TABLE stu_part(
	studente Codice NOT NULL,
	partecipazione serial NOT NULL,
	primary key (studente, partecipazione),
	foreign key (studente) references Studente(persona),
	foreign key (partecipazione) references Partecipazione(id)
);

CREATE TABLE Esame(
	codice varchar NOT NULL,
	periodo Periodo NOT NULL,
	tipo TipoEsame NOT NULL,
	partecipazione serial NOT NULL,
	studente Codice NOT NULL,
	blocco serial NOT NULL,
	primary key (studente, blocco),
	foreign key (partecipazione) references Partecipazione(id),
	foreign key (studente) references Studente(persona),
	foreign key (blocco) references Blocco(id)
);

CREATE TABLE Modulo(
	id serial NOT NULL,
	nome varchar NOT NULL,
	docente_insegnante Codice NOT NULL,
	edizione_erogatrice Integer NOT NULL,
	blocco_di_appartenenza serial NOT NULL,
	primary key (id),
	foreign key (docente_insegnante) references Docente(persona),
	foreign key (edizione_erogatrice) references Edizione(anno),
	foreign key (blocco_di_appartenenza) references Blocco(id)
);

CREATE TABLE Prova (
	id serial NOT NULL,
	voto Votazione NOT NULL,
	date timestamp NOT NULL,
	nome varchar NOT NULL,
	partecipazione serial NOT NULL,
	esame varchar NOT NULL,
	primary key (id),
	foreign key (partecipazione) references Partecipazione(id),
	foreign key (esame) references Esame(codice)
);

CREATE TABLE propedeuticità(
	precedente serial NOT NULL,
	successivo serial NOT NULL,
	primary key (precedente, successivo),
	foreign key (precedente) references Blocco(id),
	foreign key (successivo) references Blocco(id)
)











