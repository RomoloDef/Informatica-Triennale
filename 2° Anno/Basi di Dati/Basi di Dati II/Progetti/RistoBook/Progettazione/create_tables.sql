CREATE TABLE TipologiaCucina(
    id serial NOT NULL,
    nome varchar NOT NULL,
    cucina varchar NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (cucina) REFERENCES Cucina(nome)
);

CREATE TABLE Cucina(
    id serial NOT NULL,
    nome varchar NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES rist_cuc(cucina)
);

CREATE TABLE rist_cuc(
    ristorante varchar NOT NULL,
    cucina serial NOT NULL,
    PRIMARY KEY (ristorante, cucina),
    FOREIGN KEY (ristorante) REFERENCES Ristorante(partita_iva),
    FOREIGN KEY (cucina) REFERENCES Cucina(id)
);

CREATE TABLE Ristorante(
    nome varchar NOT NULL,
    indirizzo Indirizzo NOT NULL,
    partita_iva varchar NOT NULL,
    città varchar NOT NULL,
    PRIMARY KEY (partita_iva),
    FOREIGN KEY (città) REFERENCES Città(nome)
);

CREATE TABLE Città(
    nome varchar NOT NULL,
    nazione varchar NOT NULL,
    PRIMARY KEY (nome),
    FOREIGN KEY (nazione) REFERENCES Nazione(nome)
);

CREATE TABLE Nazione(
    nome varchar NOT NULL,
    PRIMARY KEY (nome)
);

CREATE TABLE rist_disp(
    ristorante varchar NOT NULL,
    disponibilità varchar NOT NULL,
    PRIMARY KEY (ristorante, disponibilità),
    FOREIGN KEY (ristorante) REFERENCES Ristorante(partita_iva),
    FOREIGN KEY (disponibilità) REFERENCES Disponibilità(nome)
);

CREATE TABLE Disponibilità(
    valore range NOT NULL,
    PRIMARY KEY (valore)
);

CREATE Table Promozione(
    id serial NOT NULL,
    massimo Int_gz_not_null NOT NULL,
    periodo_validità Periodo NOT NULL,
    sconto Real_gz_not_null NOT NULL,
    ristorante varchar NOT NULL,
    prenotazione serial NOT NULL,
    PRIMARY KEY (id), 
    FOREIGN KEY (ristorante) REFERENCES Ristorante(partita_iva),
    FOREIGN KEY (prenotazione) REFERENCES Prenotazione(id)
);

CREATE TABLE Prenotazione(
    id serial NOT NULL,
    giorno timestamp NOT NULL,
    ora timestamp NOT NULL,
    numero_commensali Int_gz_not_null NOT NULL,
    ristorante varchar NOT NULL,
    cliente varchar NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (ristorante) REFERENCES Ristorante(partita_iva),
    FOREIGN KEY (cliente) REFERENCES Cliente(email)
);

CREATE TABLE Cliente(
    nome varchar NOT NULL,
    email varchar NOT NULL,
    PRIMARY KEY (email)
);

CREATE TABLE EventoPrenotazione(
    prenotazione serial NOT NULL,
    istante timestamp NOT NULL,
    stato varchar NOT NULL,
    PRIMARY KEY (prenotazione, istante),
    FOREIGN KEY (prenotazione) REFERENCES Prenotazione(id),
    FOREIGN KEY (stato) REFERENCES StatoPrenotazione(nome)
);

CREATE TABLE StatoPrenotazione(
    nome varchar NOT NULL,
    pendente boolean NOT NULL,
    PRIMARY KEY (nome)
);

CREATE TABLE transizione(
    da varchar NOT NULL,
    a varchar NOT NULL,
    FOREIGN KEY (da) REFERENCES StatoPrenotazione(nome),
    FOREIGN KEY (a) REFERENCES StatoPrenotazione(nome),
    PRIMARY KEY (da, a)
);

CREATE DOMAIN Int_gz_not_null AS integer
    CHECK (VALUE > 0);

CREATE DOMAIN Real_gz_not_null AS real
    CHECK (VALUE > 0);

CREATE TYPE __Periodo__ AS (
    da date,
    a date
);

CREATE DOMAIN Periodo AS __Periodo__
    CHECK (VALUE.da < VALUE.a);

CREATE TYPE __Indirizzo__ AS (
    via varchar,
    civico varchar
);

CREATE DOMAIN Indirizzo AS __Indirizzo__
    CHECK (VALUE.via IS NOT NULL AND VALUE.civico IS NOT NULL);
