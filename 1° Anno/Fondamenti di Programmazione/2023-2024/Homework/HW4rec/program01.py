#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uno dei meccanismi utilizzati per conservare e gestire grandi
quantità di dati è costituito dai database. Esistono tantissimi
tipi di database, ma quello che ha rivoluzionato il settore è
costituito dai database organizzati secondo il modello relazionale
teorizzato da Codd ormai mezzo secolo fa. Secondo questo modello
i dati sono organizzati in tabelle e relazioni fra di esse, in
modo da ottimizzare le richieste di memoria, favorire la coerenza
dei dati e minimizzare gli errori.

Dobbiamo progettare un insieme di funzioni che implementi una
semplice forma di database relazionale di una scuola di formazione
in cui ci sono quattro tabelle, ovvero students, teachers, courses
ed exams. I database sono di tre diverse dimensioni, ovvero small,
medium e large. Le tabelle del database di dimensione dbsize sono
salvate in quattro file json <dbsize>_<nometabella>.json (ad esempio,
il db small è composto dai file small_students.json, small_teachers.json,
small_courses.json e small_exams.json). Le tabelle sono organizzate in
liste di dizionari (si veda ad esempio small_students.json) e hanno le
seguenti strutture:
    - students: chiavi stud_code, stud_name, stud_surname, stud_email
    - teachers: chiavi teach_code, teach_name, teach_surname, teach_email
    - courses: chiavi course_code, course_name, teach_code
    - exams: chiavi exam_code, course_code, stud_code, date, grade.
La relazione fra le tabelle implica che ogni riga in ognuna delle
tabelle ha un riferimento ad un'altra tabella: ad esempio, un esame
(exam_code) corrisponde ad un voto (grade) dato da un docente
(teach_code) ad uno studente (stud_code) per aver sostanuto
l'esame di un certo corso (course_code) in una certa data (date). Ogni
studente può aver sostenuto diversi esami. Ogni docente può tenere
diversi corsi. Ogni corso è tenuto da un solo docente.

Il campo stud_code è una chiave primaria per la tabella students poiché
identifica univocamente uno studente, ovvero non esistono due studenti
con lo stesso stud_code. Similmente, teach_code, course_code ed exam_code
sono le chiavi primarie rispettivamente delle tabelle teachers, courses ed
exams. Per questo motivo, tali campi vengono utilizzati per realizzare
la relazione fra le tabelle.

Inoltre, i campi in tutte le tabelle non sono mai vuoti.

Dobbiamo realizzare alcune funzioni per poter interrogare i database delle
diverse dimensioni. Quindi, le funzioni prevedono di usare sempre il
parametro dbsize di tipo stringa, che può assumere i valori 'small',
'medium' e 'large'. Le funzioni sono:
    - media_studente(stud_code, dbsize), che riceve una stud_code di
      uno studente e ritorna la media dei voti degli esami sostenuti,
      dallo studente.
    - media_corso(course_code, dbsize), che riceve un identificatore per un
      corso e ritorna la media dei voti degli esami per quel corso,
      sostenuti da tutti gli studenti.
    - media_docente(teach_code, dbsize), che riceve un identificatore
      di un docente e ritorna la media dei voti per gli esami
      sostenuti in tutti i corsi del docente.
    - studenti_brillanti(dbsize), che ritorna la lista delle matricole
      (stud_code) con una media di esami sostenuti superiore o uguale a 28,
      ordinate in modo decrescente per media e, in caso di parità, in
      ordine lessicografico per il cognome e il nome dello studente. In
      caso di ulteriore parità, si usi il valore numerico dello stud_code
      in ordine crescente.
    - stampa_esami_sostenuti(stud_code, dbsize, fileout), che riceve un
      numero di stud_code e salva nel file fileout la lista degli esami
      sostenuti dallo studente identificato dal valore stud_code.
      Le righe nel file devono essere ordinate in modo crescente
      per data di esame sostenuto e, in caso di stessa data, in ordine
      alfabetico. Il file ha una riga iniziale con il testo
       "Esami sostenuti dallo studente  <stud_surname> <stud_name>, matricola <stud_code>",
      mentre le righe seguenti hanno la seguente struttura
        "<course_name>\t<date>\t<grade>", in cui i campi sono allineati
      rispetto al nome del corso più lungo (ovvero tutte le date e
      i voti sono allineati verticalmente). La funzione ritorna
      il numero di esami sostenuti dallo studente.
    - stampa_studenti_brillanti(dbsize, fileout), che salva nel file
      fileout una riga per ogni studente con una media di esami
      sostenuti superiore o uguale a 28. Le righe nel file
      devono essere ordinate in modo decrescente per media e,
      in caso di parità, in ordine lessicografico per il
      cognome e il nome dello studente.
      Le righe nel file hanno la seguente struttura:
          "<stud_surname> <stud_name>\t<media>", in cui il valore media
      è allineato verticalmente per tutte le righe. La funzione
      ritorna il numero di righe salvate nel file.
    - stampa_verbale(exam_code, dbsize, fileout), che riceve un identificatore
      di esame e salva nel fileout le informazioni relative
      all'esame indicato, usando la seguente formula
        "Lo studente <stud_surname> <stud_name>, matricola <stud_code>, ha sostenuto in data <date> l'esame di <course_name> con il docente <teach_surname> <teach_name> con votazione <grade>."
      La funzione ritorna il voto dell'esame associato
      all'identificatore ricevuto in input.

Tutte le medie devono essere arrotondate alla seconda cifra decimale,
anche prima di ogni funzione di ordinamento.
Tutti i file devono avere encoding "utf8".
Per stampare agevolmente righe allineate considerare la funzione format con
i modificatori per l'allineamento (https://pyformat.info/#string_pad_align)
e con i parametri dinamici (https://pyformat.info/#param_align).
"""
import json

def media_studente(stud_code, dbsize):
    with open(f'{dbsize}_exams.json', 'r', encoding = 'utf-8') as f:
        esami = json.load(f)
        
        voti = []
        for esame in esami:
            if esame['stud_code'] == stud_code:
                voti.append(esame['grade'])
                
        media = sum(voti)/len(voti)
                
    return round(media, 2)


def media_corso(course_code, dbsize):
    with open(f'{dbsize}_exams.json', 'r', encoding = 'utf-8') as f:
        esami = json.load(f)
        
        voti = []
        for esame in esami:
            if esame['course_code'] == course_code:
                voti.append(esame['grade'])
                
        media = sum(voti)/len(voti)
                
    return round(media, 2)


def media_docente(teach_code, dbsize):
    with open(f'{dbsize}_courses.json', 'r', encoding = 'utf-8') as f:
        corsi = json.load(f)
        
    with open(f'{dbsize}_exams.json', 'r', encoding = 'utf-8') as f:
        esami = json.load(f)
        
    corsi_docente = []
    for corso in corsi:
        if corso['teach_code'] == teach_code:
            corsi_docente.append(corso['course_code'])
    
    voti = []
    for esame in esami:
        if esame['course_code'] in corsi_docente:
            voti.append(esame['grade'])
    
    media = sum(voti)/len(voti)
                
    return round(media, 2)


def studenti_brillanti(dbsize):
    with open(f'{dbsize}_students.json', 'r', encoding = 'utf-8') as f:
        studenti = json.load(f)
        
    with open(f'{dbsize}_exams.json', 'r', encoding = 'utf-8') as f:
        esami = json.load(f)
        
    media_studenti = {}
    for studente in studenti:
        voti = []
        for esame in esami:
            if esame['stud_code'] == studente['stud_code']:
                voti.append(esame['grade'])
        if len(voti) > 0:
            media = sum(voti) / len(voti)
        else:
            media = 0
        media_studenti[studente['stud_code']] = (media, studente['stud_surname'], studente['stud_name'])
        
    studenti_brillanti = []
    for stud_code, (media, i , i) in media_studenti.items():
        if media >= 28:
            studenti_brillanti.append(stud_code)
    
    studenti_brillanti.sort(key=lambda x: (-media_studenti[x][0], media_studenti[x][1], media_studenti[x][2], int(x)))
    
    return studenti_brillanti


def stampa_verbale(exam_code, dbsize, fileout):
    with open(f'{dbsize}_exams.json', 'r', encoding = 'utf-8') as f:
        esami = json.load(f)
    with open(f'{dbsize}_students.json', 'r', encoding = 'utf-8') as f:
        studenti = json.load(f)
    with open(f'{dbsize}_courses.json', 'r', encoding = 'utf-8') as f:
        corsi = json.load(f)
    with open(f'{dbsize}_teachers.json', 'r', encoding = 'utf-8') as f:
        docenti = json.load(f)
        
    for esame in esami:
        if esame['exam_code'] == exam_code:
            for studente in studenti:
                if studente['stud_code'] == esame['stud_code']:
                    stud_name = studente['stud_name']
                    stud_surname = studente['stud_surname']
                    stud_code = studente['stud_code']
            for corso in corsi:
                if corso['course_code'] == esame['course_code']:
                    course_name = corso['course_name']
                    for docente in docenti:
                        if docente['teach_code'] == corso['teach_code']:
                            teach_name = docente['teach_name']
                            teach_surname = docente['teach_surname']
                            break
                    break
            data = esame['date']
            voto = esame['grade']
            
            with open(fileout, 'w', encoding = 'utf-8') as f:
                f.write(f"Lo studente {stud_name} {stud_surname}, matricola {stud_code}, ha sostenuto in data {data} l'esame di {course_name} con il docente {teach_name} {teach_surname} con votazione {voto}.")
            
            return voto
        

def stampa_esami_sostenuti(stud_code, dbsize, fileout):
    with open(f'{dbsize}_students.json', encoding= 'utf-8') as file:
        studenti = json.load(file)
    with open(f'{dbsize}_exams.json', encoding= 'utf-8') as file:
        esami = json.load(file)
    with open(f'{dbsize}_courses.json', encoding= 'utf-8') as file:
        corsi = json.load(file)

    stud_name, stud_surname = None, None
    for studente in studenti:
        if studente['stud_code'] == stud_code:
            stud_name = studente['stud_name']
            stud_surname = studente['stud_surname']
            break

    if stud_name is None or stud_surname is None:
        return 0

    esami_studenti = []
    for esame in esami:
        if esame['stud_code'] == stud_code:
            for corso in corsi:
                if esame['course_code'] == corso['course_code']:
                    esami_studenti.append((corso['course_name'], esame['date'], esame['grade']))
                    break

    esami_studenti.sort(key=lambda x: (x[1], x[0]))

    massima_lunghezza = 0
    for corso, j , j in esami_studenti:
        if len(corso) > massima_lunghezza:
            massima_lunghezza = len(corso)

    with open(fileout, 'w', encoding ='utf8') as file:
        file.write(f'Esami sostenuti dallo studente {stud_surname} {stud_name}, matricola {stud_code}\n')
        for corso, data, voto in esami_studenti:
            file.write(f"{corso:<{massima_lunghezza}}\t{data:<10}\t{voto:<2}\n")

    return len(esami_studenti)


def stampa_studenti_brillanti(dbsize, fileout):
    lista_stud_code_brillanti = studenti_brillanti(dbsize)

    with open(f'{dbsize}_students.json', encoding= 'utf-8') as F:
        studenti = json.load(F)

    c = 0 # conteggio

    studenti_brillanti_info = []
    lunghezza_massima = 0

    for stud_code in lista_stud_code_brillanti:
        for studente in studenti:
            if studente['stud_code'] == stud_code:
                stud_name, stud_surname = studente['stud_name'], studente['stud_surname']
                studenti_brillanti_info.append((stud_name, stud_surname, stud_code))
                lunghezza = len(stud_name) + len(stud_surname)
                if lunghezza > lunghezza_massima:
                    lunghezza_massima = lunghezza
                break

    with open(fileout, 'w', encoding= 'utf-8') as file:
        for stud_name, stud_surname, stud_code in studenti_brillanti_info:
            media = media_studente(stud_code, dbsize)
            nomi_scritti = f'{stud_surname} {stud_name}'
            file.write(f'{nomi_scritti:<{lunghezza_massima+1}}\t{media:<10}\n')
            c += 1

    return c