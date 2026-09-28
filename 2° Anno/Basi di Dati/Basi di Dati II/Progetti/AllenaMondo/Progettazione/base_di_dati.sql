CREATE DOMAIN IntegerGZ AS Integer
	CHECK(value IS NOT NULL AND value > 0);
	
CREATE DOMAIN Integer1_5 As Integer 
    CHECK(value IS NOT NULL AND value >= 1 AND value <= 5);

CREATE TYPE Genere AS Enum ('maschio', 'femmina');

CREATE TYPE Categoria AS Enum ('piu chilometri', 'piu allenamenti');

CREATE Type Durata AS (
	inizio timestamp,
    fine timestamp
);

CREATE TABLE Peso (
	valore IntegerGZ NOT NULL,
	primary key (valore)
);

CREATE TABLE Altezza (
	valore IntegerGZ NOT NULL,
	primary key (valore)
);

CREATE TABLE Sportivo (
	nome_utente varchar NOT NULL,
	nome varchar NOT NULL,
	cognome varchar NOT NULL,
	genere Genere NOT NULL,
	data_nascita timestamp NOT NULL,
	peso IntegerGZ NOT NULL,
	altezza IntegerGZ NOT NULL,
	primary key (nome_utente),
	foreign key (peso) references Peso(valore),
	foreign key (altezza) references Altezza(valore)
);

CREATE TABLE amicizia (
	richiedente varchar NOT NULL,
	accettatore varchar NOT NULL,
	primary key (richiedente, accettatore),
	foreign key (richiedente) references Sportivo(nome_utente),
	foreign key (accettatore) references Sportivo(nome_utente)
);

CREATE TABLE Sfida (
	id serial NOT NULL,
	nome varchar NOT NULL,
	periodo Durata NOT NULL,
	durata_minima IntegerGZ NOT NULL,
	categoria Categoria NOT NULL,
	utente_creatore varchar NOT NULL,
	primary key (id),
	foreign key (utente_creatore) references Sportivo(nome_utente)
);

CREATE TABLE Squadra (
	nome varchar NOT NULL,
	primary key (nome)
);

CREATE TABLE iscritto_alla (
	sportivo varchar NOT NULL,
	squadra varchar NOT NULL,
	primary key (sportivo, squadra),
	foreign key (sportivo) references Sportivo(nome_utente),
	foreign key (squadra) references Squadra(nome)
);

CREATE TABLE SfidaSquadra (
	id serial NOT NULL,
	max_partecipanti IntegerGZ NOT NULL,
	squadra varchar NOT NULL,
	sfida serial NOT NULL,
	primary key (id),
	foreign key (squadra) references Squadra(nome),
	foreign key (sfida) references Sfida(id)
);

CREATE TABLE SfidaSingolo (
	id serial NOT NULL,
	sfida serial NOT NULL,
	primary key (id),
	foreign key (sfida) references Sfida(id)
);

CREATE TABLE partecipa (
	sportivo varchar NOT NULL,
	sfidaSingolo serial NOT NULL,
	primary key (sportivo, sfidaSingolo),
	foreign key (sportivo) references Sportivo(nome_utente),
	foreign key (sfidaSingolo) references SfidaSingolo(id)
);

CREATE TABLE Sport (
	nome varchar NOT NULL,
	descrizione varchar NOT NULL,
	primary key (nome)
);

CREATE TABLE presente (
	sport varchar NOT NULL,
	sfida serial NOT NULL,
	primary key (sport, sfida),
	foreign key (sport) references Sport(nome),
	foreign key (sfida) references Sfida(id)
);

CREATE TABLE Coordinate (
	latitudine real NOT NULL,
	longitudine real NOT NULL,
	primary key (latitudine, longitudine)
);

CREATE TABLE Percorso (
	id serial NOT NULL,
	nome varchar NOT NULL,
	descrizione varchar NOT NULL,
	istante_di_tempo timestamp NOT NULL,
	lat real NOT NULL,
	long real NOT NULL,
	primary key (id),
	foreign key (lat, long) references Coordinate(latitudine, longitudine)
);

CREATE TABLE AttivitaSportiva (
	id serial NOT NULL,
	difficolta Integer1_5 NOT NULL,
	istante_inizio timestamp NOT NULL,
	istante_fine timestamp NOT NULL,
	percorso serial NOT NULL,
	sport_esercitato varchar NOT NULL,
	sportivo_tracciatore varchar NOT NULL,
	CHECK (istante_inizio < istante_fine),
	primary key (id),
	foreign key (percorso) references Percorso(id),
	foreign key (sport_esercitato) references Sport(nome),
	foreign key (sportivo_tracciatore) references Sportivo(nome_utente)
);


