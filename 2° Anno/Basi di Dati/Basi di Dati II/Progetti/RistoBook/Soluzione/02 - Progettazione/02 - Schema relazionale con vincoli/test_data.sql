do $$
declare 
	_citta integer;
	_rist integer;
	_prom integer;

begin

-- clean all
delete from Prenotazione;
delete from periodo_promozione;
delete from Promozione;
delete from Ristorante;
delete from Utente;
delete from Citta;
delete from Nazione;






insert into Nazione(nome) values ('Italia');
insert into Citta(nome, nazione) values ('Roma', 'Italia') returning id into _citta;

insert into Utente(email, nome, is_proprietario) values ('aaa@xxx.com', 'Alice', 'TRUE');
insert into Utente(email, nome, is_proprietario) values ('cliente@xxx.com', 'Carlo', 'FALSE');

insert into Ristorante(nome, piva, indirizzo, citta, proprietario) values ('Cielo stellato', '00001', '("viale Plutone", "25/a")', _citta, 'aaa@xxx.com') returning id into _rist;
insert into Ristorante(nome, piva, indirizzo, citta, proprietario) values ('Prezzi fissi', '00001', '("viale Plutone", "23/a")', _citta, 'aaa@xxx.com');

insert into Promozione(sconto, max_coperti, riassegnabile, nome, ristorante)
	values ('0.3', '20', 'TRUE', 'Happy Hour', _rist) returning id into _prom;

insert into Promozione(sconto, max_coperti, riassegnabile, nome, ristorante)
	values ('0.99', '200', 'TRUE', 'Never offered', _rist);


insert into periodo_promozione(promozione, periodo) 
	values (_prom, 
			ROW( ROW('2025-06-01', '2025-06-30'), '0111001'::bit(7), ARRAY[ ROW('16:00', '17:00')::FasciaOraria, ROW('22:30', '23:30')::FasciaOraria ] )::PeriodoStrutturato
		   );

insert into Prenotazione(n, istante_pren, istante_serv, stato_corrente, cliente, ristorante, promozione)
	VALUES (5, '2025-05-28 18:23:00', '2025-06-03 16:35:00', 'pendente', 
			'cliente@xxx.com', _rist, _prom);


end;
$$