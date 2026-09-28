CREATE TABLE Servizio(
	id serial NOT NULL,
	nome varchar NOT NULL,
	descrizione varchar NOT NULL,
	prezzo_unitario RealGZ NOT NULL,
	primary key (id)
);

CREATE TABLE TipologiaAbbonamento(
	id serial NOT NULL,
	prezzo RealGZ NOT NULL,
	durata_giorni Integer NOT NULL,
	inizio_sottoscrizione timestamp NOT NULL,
	fine_sottoscrizione timestamp NOT NULL,
	utenti_usufruenti IntegerGZ NOT NULL,
	CHECK (inizio_sottoscrizione < fine_sottoscrizione),
	primary key (id)
);

CREATE TABLE TipologiaServizio(
	servizio serial NOT NULL,
	tipologia_abbonamento serial NOT NULL,
	id serial NOT NULL,
	sconto RealGZ NOT NULL,
	soglia_mensile IntegerGZ NOT NULL,
	CHECK (sconto > 0),
	CHECK (sconto < 1),
	primary key (id),
	foreign key (servizio) references Servizio(id),
	foreign key (tipologia_abbonamento) references TipologiaAbbonamento(id)
);

CREATE TABLE Utilizzo (
	id serial NOT NULL,
	istante_inizio timestamp NOT NULL,
	quantita IntegerGZ NOT NULL,
	tipo TipoUtilizzo NOT NULL,
	durata_minuti IntegerGZ NOT NULL,
	servizio serial NOT NULL,
	CHECK (istante_inizio < istante_inizio + (durata_minuti || ' minutes')::INTERVAL),
	primary key (id),
	foreign key (servizio) references Servizio(id)
);

CREATE TABLE Utente (
	id serial NOT NULL,
	nome varchar NOT NULL, 
	cognome varchar NOT NULL,
	data_nascita timestamp NOT NULL,
	indirizzo Indirizzo NOT NULL,
	mail Email NOT NULL,
	primary key (id)
);

CREATE TABLE Accesso(
	id serial NOT NULL,
	istante_accesso timestamp NOT NULL,
	tipo TipoAccesso NOT NULL,
	durata_minuti IntegerGZ NOT NULL,
	utilizzo serial NOT NULL,
	utente_acceduto serial NOT NULL
	CHECK (istante_accesso < istante_accesso + (durata_minuti || ' minutes')::INTERVAL),
	primary key (id),
	foreign key (utilizzo) references Utilizzo(id),
	foreign key (utente_acceduto) references Utente(id)
);

CREATE TABLE Cliente(
	id serial NOT NULL,
	primary key (id)
);

CREATE TABLE Impresa(
	partita_iva IVA NOT NULL,
	ragione_sociale varchar NOT NULL,
	cliente serial NOT NULL,
	primary key (partita_iva),
	foreign key (cliente) references Cliente(id)
);

CREATE TABLE Persona(
	partita_iva IVA NOT NULL,
	nome varchar NOT NULL,
	cognome varchar NOT NULL,
	data_nascita timestamp NOT NULL,
	cliente serial NOT NULL,
	primary key (partita_iva),
	foreign key (cliente) references Cliente(id)
);

CREATE TABLE Abbonamento(
	istante_inizio timestamp NOT NULL,
	id serial NOT NULL,
	cliente_abbonato serial NOT NULL,
	tipologia serial NOT NULL,
	primary key (id),
	foreign key (cliente_abbonato) references Cliente(id),
	foreign key (tipologia) references TipologiaAbbonamento(id)
);

CREATE TABLE Postazione(
	id serial NOT NULL,
	primary key (id)
);

CREATE TABLE Usufruisce(
	utente serial NOT NULL,
	abbonamento serial NOT NULL,
	id serial NOT NULL,
	postazione serial NOT NULL,
	primary key (id),
	foreign key (utente) references Utente(id),
	foreign key (abbonamento) references Abbonamento(id),
	foreign key (postazione) references Postazione(id)
);





