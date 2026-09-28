CREATE DOMAIN CodiceFiscale AS CHAR(16)
    CHECK (VALUE ~ '^[A-Z0-9]{16}$');

CREATE DOMAIN IntegerGZ AS INTEGER
    CHECK (VALUE > 0);

CREATE TYPE Indirizzo AS (
    via        TEXT,
    numero     TEXT,
);

CREATE TABLE Persona(
	nome varchar NOT NULL,
	cognome varchar NOT NULL,
	codice_fiscale Codice NOT NULL,
	primary key(codice_fiscale)
),

CREATE TABLE Utente(
	id serial NOT NULL,
	persona Codice NOT NULL,
	primary key(id),
	foreign key(persona) references Persona(codice_fiscale)
),

CREATE TABLE Artista(
	id serial NOT NULL,
	persona Codice NOT NULL,
	primary key(id),
	foreign key(persona) references Persona(codice_fiscale)
),

CREATE TABLE Prenotazione(
	id serial NOT NULL,
	numero IntegerGZ NOT NULL,
	istante_prenotazione timestamp NOT NULL
	utente_prenotante serial NOT NULL,
	primary key(id),
	foreign key(utente_prenotante) references Utente(id)
),

CREATE TABLE Posto(
	fila Integer NOT NULL,
	colonna Integer NOT NULL,
	primary key(fila, colonna)
),

CREATE TABLE pren_post(
	prenotazione serial NOT NULL,
	fila Integer NOT NULL,
	colonna Integer NOT NULL,
	primary key(prenotazione, fila, colonna),
	foreign key(prenotazione) references Prenotazione(id),
	foreign key(fila, colonna) references Posto(fila, colonna)
),

CREATE TABLE Intero(
	id serial NOT NULL,
	prezzo Real NOT NULL,
	prenotazione serial NOT NULL,
	fila Integer NOT NULL,
	colonna Integer NOT NULL,
	primary key (id),
	foreign key (fila) references Posto(fila)
	foreign key (colonna) references Posto(colonna)
), 

CREATE TABLE Ridotto(
	id serial NOT NULL,
	prezzo Real NOT NULL,
	prenotazione serial NOT NULL,
	fila Integer NOT NULL,
	colonna Integer NOT NULL,
	primary key (id),
	foreign key (fila) references Posto(fila),
	foreign key (colonna) references Posto(colonna)
), 

CREATE TABLE Sala(
	id serial NOT NULL,
	capienza IntegerGZ NOT NULL,
	tipologia varchar NOT NULL,
	primary key (id)
),

CREATE TABLE trovatosi(
	fila Integer NOT NULL,
	colonna Integer NOT NULL,
	sala serial NOT NULL,
	primary key (fila, colonna, sala),
	foreign key (fila, colonna) references Posto(fila, colonna),
	foreign key (sala) references Sala(id)
),

CREATE TABLE Sede(
	id serial NOT NULL,
	nome varchar NOT NULL,
	indirizzo Indirizzo NOT NULL,
	sala serial NOT NULL,
	primary key(id),
	foreign key (sala) references Sala(id)
),

CREATE TABLE Genere(
	nome varchar NOT NULL,
	primary key (nome)
),

CREATE TABLE Tipologia(
	nome varchar NOT NULL,
	primary key (nome)
),

CREATE TABLE Spettacolo(
	titolo varchar NOT NULL,
	orario timestamp NOT NULL,
	genere varchar NOT NULL,
	tipologia varchar NOT NULL,
	sede_rappresentante serial NOT NULL,
	id serial NOT NULL,
	primary key (id),
	foreign key (genere) references Genere(nome),
	foreign key (tipologia) references Tipologia(nome),
	foreign key (sede_rappresentante) references Sede(id)
),


