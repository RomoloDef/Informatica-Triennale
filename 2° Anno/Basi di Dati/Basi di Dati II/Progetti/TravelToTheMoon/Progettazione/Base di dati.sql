
CREATE TABLE Crociera(
	codice Codice NOT NULL,
	data_inizio timestamp NOT NULL,
	data_fine timestamp NOT NULL
	primary key (codice),
	CHECK(data_inizio < data_fine)
);

CREATE TABLE LunaDiMiele(
	id serial NOT NULL,
	tipo Tipo NOT NULL,
	crociera Codice NOT NULL,
	primary key(id),
	foreign key (crociera) references Crociera(codice)
);

CREATE TABLE PerFamiglia(
	id serial NOT NULL,
	bambini Booleano NOT NULL,
	crociera Codice NOT NULL,
	primary key(id),
	foreign key (crociera) references Crociera(codice)
);


CREATE TABLE Nazione(
	nome varchar NOT NULL,
	primary key(nome)
);

CREATE TABLE Citta(
	nome varchar NOT NULL,
	nazione varchar NOT NULL,
	primary key(nome),
	foreign key (nazione) references Nazione(nome)
);

CREATE TABLE Cliente(
	id serial NOT NULL,
	nome varchar NOT NULL,
	cognome varchar NOT NULL,
	eta IntegerGZ NOT NULL,
	indirizzo Indirizzo NOT NULL,
	citta_nascita varchar NOT NULL
	primary key(id),
	foreign key (citta_nascita) references Citta(nome)
);

CREATE TABLE Prenotazione(
	id serial NOT NULL,
	istante_prenotazione timestamp NOT NULL,
	numero_posti_prenotati IntegerGZ NOT NULL,
	crociera_prenotata Codice NOT NULL
	primary key (id),
	foreign key (crociera_prenotata) references Crociera(codice)
);

CREATE TABLE cliente_prenotazione(
	cliente serial NOT NULL,
	prenotazione serial NOT NULL,
	primary key (cliente, prenotazione),
	foreign key (cliente) references Cliente (id),
	foreig key (prenotazione) references Prenotazione(id)
);

CREATE TABLE NAVE(
	nome varchar NOT NULL,
	comfort IntegerGZ NOT NULL,
	max_passeggeri IntegerGZ NOT NULL,
	PRIMARY KEY(nome)
);

CREATE TABLE Itinerario(
	nome varchar NOT NULL,
	nave varchar NOT NULL,
	PRIMARY KEY(nome),
	FOREIGN KEY(nave) REFERENCES Nave(nome)
);

CREATE TABLE Continente(
	nome varchar NOT NULL,
	esotico Booleano NOT NULL,
	PRIMARY KEY(nome)
);

CREATE TABLE Destinazione(
	nome varchar NOT NULL,
	continente varchar NOT NULL,
	PRIMARY KEY(nome),
	FOREIGN KEY(continente) REFERENCES Continente(nome)
);

CREATE TABLE DestinazioneIntermedia(
	itinerario_id varchar NOT NULL,
	destinazione_id varchar NOT NULL,
	arrivo timestamp NOT NULL,
	ripartenza timestamp NOT NULL,
	PRIMARY KEY(itinerario_id, destinazione_id),
	FOREIGN KEY(itinerario_id) REFERENCES Itinerario(nome),
	FOREIGN KEY(destinazione_id) REFERENCES Destinazione(nome)
);

CREATE TABLE Partenza(
	itinerario_id varchar NOT NULL,
	destinazione_id varchar NOT NULL,
	istante timestamp NOT NULL,
	PRIMARY KEY(itinerario_id, destinazione_id),
	FOREIGN KEY(itinerario_id) REFERENCES Itinerario(nome),
	FOREIGN KEY(destinazione_id) REFERENCES Destinazione(nome)
);

CREATE TABLE Arrivo(
	itinerario_id varchar NOT NULL,
	destinazione_id varchar NOT NULL,
	istante timestamp NOT NULL,
	PRIMARY KEY(itinerario_id, destinazione_id),
	FOREIGN KEY(itinerario_id) REFERENCES Itinerario(nome),
	FOREIGN KEY(destinazione_id) REFERENCES Destinazione(nome)
);

CREATE TABLE PostoDaVedere(
	nome varchar NOT NULL,
	descrizione varchar NOT NULL,
	fascia_oraria Fascia NOT NULL,
	PRIMARY KEY(nome)
);

CREATE TABLE Tipologia(
	nome varchar NOT NULL,
	PRIMARY KEY(nome)
);

CREATE TABLE PostoDestinazione(
	posto_da_vedere_id varchar NOT NULL,
	destinazione_id varchar NOT NULL,
	PRIMARY KEY(posto_da_vedere_id, destinazione_id),
	FOREIGN KEY(posto_da_vedere_id) REFERENCES PostoDaVedere(nome),
	FOREIGN KEY(destinazione_id) REFERENCES Destinazione(nome)
);

CREATE TABLE TipologiaDestinazione(
	tipologia_id varchar NOT NULL,
	destinazione_id varchar NOT NULL,
	PRIMARY KEY(tipologia_id, destinazione_id),
	FOREIGN KEY(tipologia_id) REFERENCES Tipologia(nome),
	FOREIGN KEY(destinazione_id) REFERENCES Destinazione(nome)
);

