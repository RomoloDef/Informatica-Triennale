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

print(media_studente('1803891', 'small'))

def media_corso(course_code, dbsize):
    with open(f'{dbsize}_exams.json', 'r', encoding = 'utf-8') as f:
        esami = json.load(f)
        
        voti = []
        for esame in esami:
            if esame['course_code'] == course_code:
                voti.append(esame['grade'])
                
        media = sum(voti)/len(voti)
                
    return round(media, 2)

print(media_corso('EDIELFAC0x5203a7', 'small'))

def media_docenti(teach_code, dbsize):
    with open(f'{dbsize}_courses.json', 'r', encoding = 'utf-8') as f:
        corsi = json.load(f)
        
    with open(f'{dbsize}_exams.json', 'r', encoding = 'utf-8') as f:
        esami = json.load(f)
        
    corsi_docente = [corso['course_code'] for corso in corsi if corso['teach_code'] == teach_code]
    
    voti = [esame['grade'] for esame in esami if esame['course_code'] in corsi_docente]
    
    media = sum(voti)/len(voti) if voti else 0
                
    return round(media, 2)

print(media_docenti('002', 'small'))

def studenti_brillanti(dbsize):
    with open(f'{dbsize}_students.json', 'r', encoding = 'utf-8') as f:
        studenti = json.load(f)
        
    with open(f'{dbsize}_exams.json', 'r', encoding = 'utf-8') as f:
        esami = json.load(f)
        
    media_studenti = {}
    for studente in studenti:
        voti = [esame['grade'] for esame in esami if esame['stud_code'] == studente['stud_code']]
        media = sum(voti)/len(voti) 
        media_studenti[studente['stud_code']] = (media, studente['stud_surname'], studente['stud_name'])
        
    studenti_brillanti = [stud_code for stud_code, (media, _, _) in media_studenti.items() if media >= 28]
    
    studenti_brillanti = sorted(studenti_brillanti, key=lambda x: (-media_studenti[x][0], media_studenti[x][1], media_studenti[x][2], int(x)))
    
    return studenti_brillanti

print(studenti_brillanti('small'))

def stampa_verbale(exam_code, dbsize, fileout):
    pass
    
print(stampa_verbale('EDIELFAC0x5203a7_1803891', 'small', 'esame.txt'))


def stampa_esami_sostenuti(stud_code, dbsize, fileout):
    with open(f'{dbsize}_exams.json', 'r', encoding = 'utf-8') as f:
        esami = json.load(f)
        
    with open(f'{dbsize}_courses.json', 'r', encoding = 'utf-8') as f:
        corsi = json.load(f)
        
    esami_studente = []
    for esame in esami:
        if esame['stud_code'] == stud_code:
            esami_studente.append(esame)
            
    esami_studente.sort(key=lambda x: (x['date'], next((corso['course_name'] for corso in corsi if corso['course_code'] == x['course_code']), '')))
    
    with open(fileout, 'w', encoding = 'utf-8') as f:
        for esame in esami_studente:
            corso = next((corso for corso in corsi if corso['course_code'] == esame['course_code']), None)
            f.write(f"{corso['course_name']}\t{esame['date']}\t{esame['grade']}\n")
            
    return len(esami_studente)

print(stampa_esami_sostenuti('1803891', 'small', 'esami.txt'))

def stampa_studenti_brillanti(dbsize, fileout):
    with open(f'{dbsize}_students.json', 'r', encoding = 'utf-8') as f:
        studenti = json.load(f)
        
    with open(f'{dbsize}_exams.json', 'r', encoding = 'utf-8') as f:
        esami = json.load(f)
        
    for studente in studenti:
        esami_studente = [int(esame['grade']) for esame in esami if esame['stud_code'] == studente['stud_code']]
        studente['media'] = sum(esami_studente) / len(esami_studente) if esami_studente else 0

    studenti_brillanti = [studente for studente in studenti if studente['media'] >= 28]

    studenti_brillanti.sort(key=lambda studente: (-studente['media'], studente['stud_surname'], studente['stud_name']))

    with open(fileout, 'w', encoding = 'utf-8') as f:
        for studente in studenti_brillanti:
            f.write(f"{studente['stud_surname']} {studente['stud_name']}\t{studente['media']:.2f}\n")
            
    return len(studenti_brillanti)
            
print(stampa_studenti_brillanti('small', 'studenti.txt'))


    
  


    
                
