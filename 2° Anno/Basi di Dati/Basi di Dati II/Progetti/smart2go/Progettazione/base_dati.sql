CREATE TABLE Persona (
	id serial NOT NULL,
	nome varchar NOT NULL,
	cognome varchar NOT NULL,
	data_nascita NOT NULL,
	primary key (id)
);

CREATE TABLE Responsabile (
	id serial NOT NULL,
	persona serial NOT NULL,
	primary key (id),
	foreign key (persona) references Persona(id)
);

CREATE TABLE Societa (
	nome varchar NOT NULL,
	iban IBAN NOT NULL,
	indirizzo Indirizzo NOT NULL,
	responsabile serial NOT NULL,
	primary key (iban),
	foreign key (responsabile) NOT NULL
);

CREATE TABLE SmartCard (
	codice varchar NOT NULL,
	primary key (codice)
);

CREATE TABLE Socio (
	persona serial NOT NULL,
	estremi_patente varchar NOT NULL,
	smartcard varchar NOT NULL,
	primary key (estremi_patente),
	foreign key (persona) references Persona(id),
	foreign key (smartcard) references SmartCard(codice)
);

CREATE TABLE Privato (
	id serial NOT NULL,
	numero_carta_credito varchar NOT NULL,
	indirizzo_residenza Indirizzo NOT NULL,
	socio varchar NOT NULL,
	primary key (id),
	foreign key (socio) references Socio(estremi_patente)
);

CREATE TABLE Dipendente (
	id serial NOT NULL,
	socio varchar NOT NULL,
	societa IBAN NOT NULL,
	primary key (id),
	foreign key (socio) references Socio(estremi_patente),
	foreign key (societa) references Societa(Iban)
);

CREATE TABLE Convenzioni (
	id serial NOT NULL,
	nome varchar NOT NULL,
	tass_sconto Sconto NOT NULL,
	societa IBAN NOT NULL,
	primary key (id),
	foreign key (societa) references Societa(Iban)
);

CREATE TABLE GPS (
	coordinate Coordinate NOT NULL,
	primary key (coordinate)
);

CREATE TABLE Categoria (
	nome varchar NOT NULL,
	primary key (nome)
);

CREATE TABLE Auto (
	targa Targa NOT NULL,
	modello varchar NOT NULL,
	numero_posti IntegerGZ NOT NULL,
	data_ultima_manutenzione Data NOT NULL,
	eventuali_danni varchar NOT NULL,
	gps Coordinate NOT NULL,
	categoria varchar NOT NULL,
	primary key (targa),
	foreign key (gps) references GPS(coordinate),
	foreign key (categoria) references Categoria(nome)
);

CREATE TABLE AutoParcheggiata (
	id serial NOT NULL,
	auto Targa NOT NULL,
	primary key (id),
	foreign key (auto) references Auto(targa)
);

CREATE TABLE AutoNoleggiata (
	id serial NOT NULL,
	auto Targa NOT NULL,
	primary key (id),
	foreign key (auto) references Auto(targa)
);

CREATE TABLE AutoTradizionale (
	id serial NOT NULL,
	chilometri_a_litro IntegerGZ NOT NULL,
	auto Targa NOT NULL,
	primary key (id),
	foreign key (auto) references Auto(targa)
);

CREATE TABLE AutoEcompatibile (
	id serial NOT NULL,
	autonomia IntegerGZ NOT NULL,
	tipo_alimentazione varchar NOT NULL,
	auto Targa NOT NULL,
	primary key (id),
	foreign key (auto) references Auto(targa)
);

CREATE TABLE ConvenzioniTradizionali (
	id serial NOT NULL,
	convenzione serial NOT NULL,
	autoTradizionale serial NOT NULL,
	primary key (id),
	foreign key (convenzione) references Convenzioni(id)
	foreign key (autoTradizionale) references AutoTradizionale(id)
);

CREATE TABLE ConvenzioniEcompatibili (
	id serial NOT NULL,
	convenzione serial NOT NULL,
	autoEcompatibile serial NOT NULL,
	primary key (id),
	foreign key (convenzione) references Convenzioni(id)
	foreign key (autoEcompatibile) references AutoEcompatibile(id)
);

CREATE TABLE Noleggio (
	id serial NOT NULL,
	quota_al_minuto RealGZ NOT NULL,
	istante_inizio timestamp NOT NULL,
	auto Targa NOT NULL,
	primary key (id),
	foreign key (auto) references Auto(targa)
);

CREATE TABLE effettua (
	socio varchar NOT NULL,
	noleggio serial NOT NULL,
	primary key (socio, noleggio),
	foreign key (socio) references Socio(estremi_patente),
	foreign key (noleggio) references Noleggio(id)
);

CREATE TABLE nol_conv (
	noleggio serial NOT NULL,
	convenzione serial NOT NULL,
	primary key (noleggio, convenzione),
	foreign key (noleggio) references Noleggio(id),
	foreign key (convenzione) references Convenzioni(id)
);

CREATE TABLE Sinistri (
	descrizione varchar NOT NULL,
	quando timestamp NOT NULL,
	luogo Indirizzo NOT NULL,
	feriti Boolean NOT NULL,
	danni_economici IntegerGZ NOT NULL,
	noleggio serial NOT NULL,
	id serial NOT NULL,
	primary key (id),
	foreign key (noleggio) references Noleggio(id)
);

CREATE TABLE SinistrisenzaControParte (
	id serial NOT NULL,
	sinistro serial NOT NULL,
	primary key (id),
	foreign key (sinistro) references Sinistri(id)
);

CREATE TABLE SinistriConControparte (
	id serial NOT NULL,
	sinistro serial NOT NULL,
	primary key (id),
	foreign key (sinistro) references Sinistri(id)
);



