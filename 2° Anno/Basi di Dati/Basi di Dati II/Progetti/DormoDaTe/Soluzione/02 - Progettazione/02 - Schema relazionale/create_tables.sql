CREATE TABLE TipoRisorsaGeografica(
	nome Stringa NOT NULL,
	primary key nome
);
INSERT INTO TipoRisorsaGeografica(nome) VALUES ('centro');

CREATE FUNCTION Fun_trigger_solleva_eccezione RETURNS TRIGGER ...
	raise Exception...

CREATE TRIGGER Trigger_TipoRisorsaGeografica_la_ennupla_centro_non_si_tocca
	BEFORE UPDATE OR DELETE ON TipoRisorsaGeografica
	FOR EACH ROW 
		WHEN new.nome = 'centro' or old.nome = 'centro'
			EXECUTE PROCEDURE Fun_trigger_solleva_eccezione()
	...


-- Da completarsi per esercizio