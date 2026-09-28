CREATE TABLE Nazione(
	nome Stringa NOT NULL,
	primary key (nome)
);	

CREATE TABLE Citta(
	id serial NOT NULL, 
	nome Stringa NOT NULL, 
	nazione Stringa NOT NULL,
	primary key (id),
	foreign key (nazione) references Nazione(nome)
);

CREATE TABLE Utente(
	email Email NOT NULL,
	nome Stringa NOT NULL,
	is_proprietario Boolean NOT NULL,
	primary key (email),	
	unique (email, is_proprietario) 
)

CREATE TABLE Ristorante(
	id serial NOT NULL, 
	nome Stringa NOT NULL, 
	piva PartitaIVA NOT NULL, 
	indirizzo Indirizzo NOT NULL, 
	citta integer NOT NULL,
	proprietario Email NOT NULL,
	prop_is_proprietario Boolean NOT NULL GENERATED ALWAYS AS (TRUE) STORED,
	primary key (id),
	foreign key (citta) references Citta(id),
	foreign key (proprietario, prop_is_proprietario) references Utente(email, is_proprietario)
);

CREATE TABLE apertura(
	ristorante integer NOT NULL,  
	val_apertura PeriodoStrutturato NOT NULL,
	primary key (ristorante, val_apertura),
	foreign key (ristorante) references Ristorante(id)
);	


CREATE TABLE TipologiaCucina(
	nome Stringa NOT NULL,
	primary key (nome)
);	

CREATE TABLE rist_tipocuc(
	ristorante integer NOT NULL, 
	tipocuc Stringa NOT NULL,
	primary key (ristorante, tipocuc),
	foreign key (ristorante) references Ristorante(id),
	foreign key (tipocuc) references TipologiaCucina(nome)
);

CREATE TABLE Promozione(
	id serial NOT NULL, 
	sconto Sconto NOT NULL, 
	max_coperti IntegerGZ NOT NULL, 
	riassegnabile BOOLEAN NOT NULL, 
	nome Stringa NOT NULL,
	ristorante integer NOT NULL,
	primary key (id),
	foreign key (ristorante) references Ristorante(id)
);	

CREATE TABLE periodo_promozione(
	promozione integer NOT NULL, 
	periodo PeriodoStrutturato NOT NULL,
	foreign key (promozione) references Promozione(id)
);

CREATE TABLE Prenotazione(
	id serial NOT NULL,	
	n IntegerGZ NOT NULL,

	istante_pren timestamp NOT NULL,
	istante_serv timestamp NOT NULL,

	stato_corrente StatoPrenotazione NOT NULL,

	istante_ann timestamp NULL,
	istante_acc timestamp NULL,
	istante_rif timestamp NULL,
	istante_compl timestamp NULL,
	istante_nonutil timestamp NULL,

	cliente Email NOT NULL,
	ristorante integer NOT NULL,
	promozione integer NULL,

	primary key (id),
	foreign key (cliente) references Utente(email), -- accorpa cl_pren
	foreign key (ristorante) references Ristorante(id), -- accorpa pren_rist
	foreign key (promozione) references Promozione(id), -- accorpa pren_prom

	check (istante_pren < istante_serv),

	check (istante_compl is null or istante_acc is not null), -- se completata --> allora accettata
	check (istante_nonutil is null or istante_acc is not null) -- se non util. --> allora accettata
	-- tutti gli altri...
);	