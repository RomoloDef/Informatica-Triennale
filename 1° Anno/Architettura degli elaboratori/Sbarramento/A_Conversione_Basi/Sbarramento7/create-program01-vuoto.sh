#!/bin/bash
echo -n "" > "program01.vuoto.asm"
stop_at="## INSERIRE IL PROPRIO CODICE QUI"

# Copia fino all'occorrenza della riga $stop_at
sed "/^$stop_at$/q" program01.asm >> "program01.vuoto.asm"
sed -E 's|^# Matricola:[[:space:]]*[0-9]+$|# Matricola:|' program01.vuoto.asm > temp
mv temp program01.vuoto.asm
rm -f temp

echo >> "program01.vuoto.asm"