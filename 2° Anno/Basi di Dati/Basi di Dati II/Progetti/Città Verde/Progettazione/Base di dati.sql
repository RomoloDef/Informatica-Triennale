CREATE TABLE Operatore (
	id serial NOT NULL,
	nome varchar NOT NULL,
	cognome timestamp NOT NULL,
	codice_fiscale CodiceFiscale NOT NULL,
	tipo TipoOperatore NOT NULL,
	data_inizio_servizio timestamp NOT NULL,
	data_fine_servizo timestamp,
	CHECK (data_inizio_servizio < data_fine_servizio),
	PRIMARY KEY (id)
);

CREATE TABLE Attrezzatura(
	id serial NOT NULL,
	nome varchar NOT NULL,
	tipologia Tipologia NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE utilizza(
	operatore serial NOT NULL,
	attrezzatura serial NOT NULL,
	PRIMARY KEY (operatore, attrezzatura),
	FOREIGN KEY (operatore) references Operatore(id),
	FOREIGN KEY (attrezzatura) references Attrezzatura(id)
);

CREATE TABLE Squadra(
	codice_identificativo Codice NOT NULL,
	data_formazione timestamp NOT NULL,
	membri IntegerGZ NOT NULL,
	tipo TipoSquadra NOT NULL,
	data_scioglimento timestamp,
	operatore_lavoratore serial NOT NULL,
	capo serial NOT NULL,
	CHECK (data_formazione < data_scioglimento),
	PRIMARY KEY (codice_identificativo),
	FOREIGN KEY (operatore) references Operatore(id),
	FOREIGN KEY (capo) references Capo(id)
);

CREATE TABLE AreaVerde(
	id serial NOT NULL,
	denominazione varchar NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Intervento(
	id serial NOT NULL,
	data_inizio timestamp NOT NULL,
	durata_attesa Durata NOT NULL,
	tipologia TipologiaAtt NOT NULL,
	priorita Integer NOT NULL,
	minimo_operatore IntegerGZ NOT NULL,
	istante_acquisizione timestamp NOT NULL,
	tipo TipoIntervento NOT NULL,
	istante_completamento timestamp,
	attrezzatura serial NOT NULL,
	squadra Codice NOT NULL,
	area_verde serial NOT NULL,
	CHECK (istante_acquisizione < istante_completamento),
	CHECK (priorita >= 0),
	CHECK (priorita <= 10),
	PRIMARY KEY (id),
	FOREIGN KEY (attrezzatura) references Attrezzatura(id),
	FOREIGN KEY (squadra) references Squadra(codice_identificativo),
	FOREIGN KEY (area_verde) references AreaVerde(id) 
);

CREATE TABLE AreaNonFruibile(
	id serial NOT NULL,
	nome varchar NOT NULL,
	area_verde serial NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (area_verde) references AreaVerde(id) 
);

CREATE TABLE AreaFruibile(
	id serial NOT NULL,
	nome varchar NOT NULL,
	tipo TipoAreaFruibile NOT NULL,
	area_verde serial NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (area_verde) references AreaVerde(id) 
);

CREATE TABLE SoggettoVerde(
	id serial NOT NULL,
	data_piantificazione timestamp NOT NULL,
	posizione Coordinate NOT NULL,
	specie Specie NOT NULL,
	categoria_rischio Rischio NOT NULL,
	tipo TipoPianta NOT NULL,
	data_rimozione timestamp,
	causa Causa,
	area_contenente serial NOT NULL,
	CHECK (data_piantificazione < data_rimozione),
	PRIMARY KEY (id),
	FOREIGN KEY (area_contenente) references AreaVerde(id) 
);

CREATE TABLE DimensioniFisiche(
	nome varchar NOT NULL,
	unita_misura varchar NOT NULL,
	PRIMARY KEY (nome)
);

CREATE TABLE ValoreDimensione(
	soggetto_verde serial NOT NULL,
	dimensione varchar NOT NULL,
	valore real NOT NULL,
	PRIMARY KEY (soggetto_verde, dimensione),
	FOREIGN KEY (soggetto_verde) references SoggettoVerde(id),
	FOREIGN KEY (dimensione) references DimensioniFisiche(nome)
);

CREATE TABLE PiantaMalata (
	id serial NOT NULL,
	tipo TipoPiantaMalata NOT NULL,
	intervento timestamp NOT NULL,
	guarigione varchar NOT NULL,
	soggetto_verde serial NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (soggetto_verde) references SoggettoVerde(id)
);

CREATE TABLE EpisodioMalattia (
	id serial NOT NULL,
	data_scoperta timestamp NOT NULL,
	risoluzione boolean NOT NULL,
	pianta_malata serial NOT NULL,
	pianta_malata_curata serial,
	PRIMARY KEY (id),
	FOREIGN KEY (pianta_malata) references PiantaMalata(id),
	FOREIGN KEY (pianta_malata_curata) references PiantaMalata(id)
);

CREATE TABLE Malattia (
	id serial NOT NULL,
	nome_scientifico varchar NOT NULL,
	nome_volgare varchar NOT NULL,
	gravita Gravita NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE successo (
	malattia serial NOT NULL,
	episodio serial NOT NULL,
	PRIMARY KEY (malattia, episodio),
	FOREIGN KEY (malattia) references Malattia(id),
	FOREIGN KEY (episodio) references EpisodioMalattia(id)
)
