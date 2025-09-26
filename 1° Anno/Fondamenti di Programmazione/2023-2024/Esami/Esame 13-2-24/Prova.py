D = {4: ["c", "h", "f", "g", "e"], 2: ["a", "z", "b", "w"], 0: ["a", "b", "a"]}
risultato = []
for chiave, valore in D.items():
    valore.sort(reverse = True)
    risultato.append(valore[chiave])
print(risultato)
    