anno=$(cd ../../ && basename "`pwd`")
anno=`echo $anno | awk '{split($0,a,"_"); print a[2]}' | awk '{OFS = "/";split($0,a,"-"); print a[1],a[2]}'`
EXAM_ID="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
EXAM_ID=`basename "${EXAM_ID}"`
data=`echo $EXAM_ID | awk '{split($0,a,"_"); print a[3]}' | awk '{OFS = "/";split($0,a,"-"); print a[3],a[2],a[1]}'`
echo "Generazione del README file in corso..."
echo "Data: $data"
echo "Anno accademico: $anno"
echo "# Architettura degli Elaboratori a.a. "$anno >temp.md
echo "## Appello d'esame "$data" (ASM)">>temp.md
cat README.md >> temp.md
sed -e '/{{max-iter.expt}}/ {r max-iter.expt' -e 'd }' temp.md > temp2.md
pandoc temp2.md -V geometry:margin=1.3in -o README.pdf
echo "Creazione di README.pdf completato. Rimozione dei file temporanei in corso..."
rm -f temp.md
rm -f temp2.md
echo "Fatto."
if [ -f "README_ENG.md" ]; then
    echo "Generating English version TODO"
fi