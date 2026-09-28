CREATE TABLE Nazione (
	nome varchar NOT NULL,
	primary key (nome)
);

CREATE TABLE Regione (
	nome varchar NOT NULL,
	nazione varchar NOT NULL,
	foreign key (nazione) references Nazione(nome),
	primary key (nome)
);

CREATE TABLE Citta(
	nome varchar NOT NULL,
	regione varchar NOT NULL,
	foreign key (regione) references Regione(nome),
	primary key (nome)
);

CREATE TABLE Utente(
	id serial NOT NULL,
	nome varchar NOT NULL,
	cognome varchar NOT NULL,
	email varchar NOT NULL,
	data_iscrizione timestamp NOT NULL,
	citta_appartenenza varchar NOT NULL,
	primary key (id),
	foreign key (citta_appartenenza) references Citta(nome)
);

CREATE TABLE Viaggio(
	id serial NOT NULL,
	nome varchar NOT NULL,
	numero_minimo integer NOT NULL,
	numero_massimo integer NOT NULL,
	utente serial NOT NULL,
	CHECK (numero_minimo < numero_massimo),
	primary key(id),
	foreign key (utente) references Utente(id)
);

CREATE TABLE UtenteOrganizzatore (
	id serial NOT NULL,
	utente serial NOT NULL,
	viaggio serial NOT NULL,
	voto integer NOT NULL,
	CHECK (voto > 1),
	CHECK (voto < 5),
	primary key (id),
	foreign key (utente) references Utente(id),
	foreign key (viaggio) references Viaggio(id)
);

CREATE TABLE Attivita (
	id serial NOT NULL,
	nome varchar NOT NULL,
	istante_inizio timestamp NOT NULL,
	durata timestamp NOT NULL,
	biglietti varchar NOT NULL,
	primary key (id)
);

CREATE TABLE possiede (
	viaggio serial NOT NULL,
	attivita serial NOT NULL,
	primary key (attivita),
	foreign key (viaggio) references Viaggio(id),
	foreign key (attivita) references Attivita(id)
);

CREATE TABLE Luogo(
	id serial NOT NULL,
	indirizzo varchar NOT NULL,
	primary key (id)
);

CREATE TABLE att_luo(
	attivita serial NOT NULL,
	luogo serial NOT NULL,
	primary key (attivita, luogo),
	foreign key (attivita) references Attivita(id),
	foreign key (luogo) references Luogo(id)
);

CREATE TABLE citt_luo(
	citta varchar NOT NULL,
	luogo serial NOT NULL,
	primary key (citta, luogo),
	foreign key (citta) references Citta(nome),
	foreign key (luogo) references Luogo(id)
);

CREATE TABLE Pernottamenti(
	id serial NOT NULL,
	attivita serial NOT NULL,
	primary key (id),
	foreign key (attivita) references Attivita(id)
);

CREATE TABLE Spostamenti(
	id serial NOT NULL,
	tipo varchar NOT NULL,
	luogo_partenza serial NOT NULL,
	luogo_arrivo serial NOT NULL,
	primary key (id),
	foreign key (luogo_partenza) references Luogo(id),
	foreign key (luogo_arrivo) references Luogo(id)
);

CREATE TABLE MezzoSpostamento(
	nome varchar NOT NULL,
	spostamenti serial NOT NULL,
	primary key (nome),
	foreign key (spostamenti) references Spostamenti(id)
);



