#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Il tuo caro amico Pico de Paperis ti ha mandato un messaggio molto strano scarabocchiato su una cartolina.
Ê da tanto che non lo vedi e da sempre vi divertite a scrivervi in codice.
Per decodificare il suo messaggio vai a cercare nella tua biblioteca un libro un po' particolare,
il cifrario di Archimede Pitagorico. Il cifrario da applicare è la famosa "Cifra del Faraone".
La decifrazione col metodo del Faraone si basa su delle regole di sostituzione di sequenze di simboli nel testo.
Il motivo per cui si chiama "cifra del Faraone" è che in antico Egizio le sequenze formate da più geroglifici
potevano essere scritte in qualsiasi ordine, quindi ogni anagramma delle sequenze era valido.
Per rendere la cosa più strana, Pico de Paperis ha deciso di usare un cifrario che non è esattamente quello del
Faraone, ma una sua variante. Invece di usare gli anagrammi usa dei "quasi anagrammi", cioè anagrammi che nel testo
originale hanno un carattere spurio in più rispetto alla sequenza cercata.
Nel cifrario sono contenute coppie di sequenze che indicano come trasformare il testo.
Ad esempio la coppia 'shampoo' -> 'soap' corrisponde a cercare un punto del messaggio in cui appare la sequenza 'shampoo'
(o un suo anagramma) ma con un carattere in più (ad esempio 'pmQohaso') e sostituirla con la sequenza 'soap'.

La decodifica del messaggio può portare a più possibili messaggi finali, perchè possono esserci più sequenze nel testo
che possono essere trasformate in ogni momento e l'ordine delle trasformazioni influenza le trasformazioni successive.
Ad un certo punto succederà che nessun "quasi-anagramma" delle sequenze del cifrario è presente in nessun punto
della sequenza di simboli per cui non è più possibile fare trasformazioni.
Queste sequenze le chiamiamo sequenze finali.
Di tutte le possibili sequenze finali,ci interessa l'insieme delle più corte.

Per decodificare il messaggio di Pico de Paperis devi implementare la funzione
pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
che riceve come argomenti:
- il testo che ti ha mandato Pico de Paperis, come stringa di simboli (caratteri)
- il cifrario da applicare, un dizionario che ha come chiavi le sequenze di cui cercare nel testo un quasi-anagramma
   e come valore associato la stringa da sostituire al quasi-anagramma trovato.
la funzione deve tornare l'insieme dei più brevi testi ottenibili applicando ripetutamente
le trasformazioni fin quando non è più possibile applicarne nessuna.

Esempio:
encrypted_text  = 'astronaut-flying-cyrcus'
pharaohs_cypher = {'tuar': 'me', 'cniy': 'op', 'sorta': 'tur', 'fult': 'at', 'rycg': 'nc'}

Risultato: {'tmeopcus', 'metopcus', 'ameopcus', 'atmepcus'}
e tutte le trasformazioni applicate sono quelle contenute nel file example.txt
(in ordine alfabetico e senza ripetizioni)

NOTA: almeno una delle funzioni o metodi che realizzate deve essere ricorsiva
NOTA: la funzione/metodo ricorsivo/o deve essere definita a livello più esterno
      altrimenti fallirete il test di ricorsione.
'''

def verifica_anagramma(chiave:str, quasi_anagramma:str) -> bool:
    # 1° controllo sulla lunghezza della chiave e della sequenza di caratteri
    if len(chiave) + 1 != len(quasi_anagramma):
        return False
    # itero per ogni carattere nella chiave del dizionario
    for c in chiave:
        if chiave.count(c) > quasi_anagramma.count(c):
            return False
    return True

# funzione ricorsiva per tradurre l'encrypted test in nuove stringhe
def decodifica(encrypted_text: str, pharaohs_cypher: dict[str, str]) -> set[str]:
    insieme = set()
    # itero per chiave e valore del dizionario dato in input
    for chiave, valore in pharaohs_cypher.items():
        l = len(chiave) + 1
        for i in range(len(encrypted_text)-l+1):
            s = encrypted_text[i:i+l]
            if verifica_anagramma(chiave, s):
                # richiamando la funzione che verifica la stringa col quasi anagramma costruisco la mia nuova stringa tramite le slice
                nuova_stringa = encrypted_text[:i] + valore + encrypted_text[i+l:]
                # aggiungo all'insieme tutte le stringhe con le sostituzioni
                insieme.update(decodifica(nuova_stringa, pharaohs_cypher))
    # caso base
    if len(insieme) == 0:
        insieme.add(encrypted_text)
    return insieme

def pharaohs_revenge(encrypted_text: str, pharaohs_cypher: dict[str, str]) -> set[str]:
    # richiamo la funzione precedente
    stringhe = decodifica(encrypted_text, pharaohs_cypher)
    # verifico quali sono le lunghezze minime di tutte le stringhe minime
    lunghezza_minima = len(min(stringhe, key=len))
    # ritorno un dizionario contenente le stringhe con lunghezza minima
    return {stringa for stringa in stringhe if len(stringa) == lunghezza_minima}



if __name__ == '__main__':
    pharaohs_revenge('astronaut-flying-cyrcus', {'tuar': 'me', 'cniy': 'op', 'sorta': 'tur', 'fult': 'at', 'rycg': 'nc'})
    pass
    # inserisci qui i tuoi test personali