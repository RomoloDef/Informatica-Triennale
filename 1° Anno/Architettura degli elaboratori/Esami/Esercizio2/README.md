# ⚡ Esercizio 2: CPU RISC-V a Ciclo Singolo ed Estensione Datapath

Questa cartella raccoglie le tracce e i testi d'esame in formato immagine relativi al **secondo esercizio** della prova scritta di Architettura degli Elaboratori.

---

## 📌 Contenuto della Cartella

- [Esercizio 2-1.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio2/Esercizio%202-1.png): Traccia Appello 1 (`lwig`)
- [Esercizio 2-2.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio2/Esercizio%202-2.png): Traccia Appello 2 (`bltsafe`)
- [Esercizio 2-3.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio2/Esercizio%202-3.png): Traccia Appello 3 (`jalf`)
- [Esercizio 2-4.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio2/Esercizio%202-4.png): Traccia Appello 4 (`msum`)
- [Esercizio 2-5.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio2/Esercizio%202-5.png): Traccia Appello 5 (`beqi`)
- [Esercizio 2-6.png](file:///Users/romolodeffereria/Desktop/Architettura/Esami/Esercizio2/Esercizio%202-6.png): Traccia Appello 6 (`seq`)

---

## 🛠️ Come si Risolve l'Esercizio 2

L'esercizio 2 presenta sempre la medesima struttura logica: viene descritta una nuova istruzione assembly inventata ad-hoc e viene richiesto di:

1. **Modificare lo schema del Datapath RISC-V a ciclo singolo:**
   - Individuare i registri sorgente (`rs1`, `rs2`), il registro destinazione (`rd`), gli operandi immediati o gli accessi a memoria richiesti.
   - Aggiungere eventuali multiplexer (es. per selezionare ingressi alternativi all'ALU o per la scrittura nel Register File), sommatori dedicati o unità logiche ausiliarie.
   - Disegnare le nuove linee dati evidenziando la loro provenienza e destinazione.
2. **Definire la Tabella dei Segnali di Controllo:**
   - Specificare i valori dei segnali standard (`RegWrite`, `ALUSrc`, `MemRead`, `MemWrite`, `MemtoReg`, `Branch`, `ALUOp`) per la nuova istruzione e definire eventuali nuovi segnali di controllo necessari per pilotare i multiplexer introdotti.
3. **Scrivere la Instruction Word a 32 bit:**
   - Scegliere il formato d'istruzione corretto tra i tipi RISC-V:
     - **Tipo R:** `[funct7: 7 bit] [rs2: 5 bit] [rs1: 5 bit] [funct3: 3 bit] [rd: 5 bit] [opcode: 7 bit]`
     - **Tipo I:** `[imm[11:0]: 12 bit] [rs1: 5 bit] [funct3: 3 bit] [rd: 5 bit] [opcode: 7 bit]`
     - **Tipo S:** `[imm[11:5]: 7 bit] [rs2: 5 bit] [rs1: 5 bit] [funct3: 3 bit] [imm[4:0]: 5 bit] [opcode: 7 bit]`
     - **Tipo B:** `[imm[12|10:5]: 7 bit] [rs2: 5 bit] [rs1: 5 bit] [funct3: 3 bit] [imm[4:1|11]: 5 bit] [opcode: 7 bit]`
     - **Tipo U / J:** Immediato esteso a 20 bit.
   - Assegnare un valore numerico coerente ai campi (opcode libero o specificato dalla consegna).

---

## 📖 Soluzioni e Risoluzioni Complete
Nel file [GuidaEsercizio2.pdf](file:///Users/romolodeffereria/Desktop/Architettura/Esami/GuidaEsercizio2.pdf) sono riportate le spiegazioni dettagliate, gli schemi e le tabelle di verità per tutte e 6 le istruzioni degli appelli.
