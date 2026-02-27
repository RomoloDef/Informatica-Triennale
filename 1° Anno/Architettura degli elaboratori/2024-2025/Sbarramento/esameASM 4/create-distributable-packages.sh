chmod +x *.sh
EXAM_ID="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
EXAM_ID=`basename "${EXAM_ID}"`
temp=`echo $EXAM_ID | awk '{split($0,a,"_"); print a[3]}' | awk '{OFS = "-";split($0,a,"-"); print a[3],a[2],substr (a[1],3,5)}'`
VM_EXAM_ID='esame-ASM-'$temp
#
make clean
mkdir ./esameASM
cp *.expt ./esameASM/.
cp *.in ./esameASM/.
bash create-program01-vuoto.sh
bash create-README.pdf.sh
cp program01.vuoto.asm ./esameASM/.
cp program01.vuoto.asm ./esameASM/program01.asm
cp *.pdf ./esameASM/.
cp run.sh ./esameASM/.
echo "RARS:=java -jar ./rars1_6.jar" > ./esameASM/Makefile && tail -n +2 Makefile >> ./esameASM/Makefile
cp ../../rars1_6.jar ./esameASM/rars1_6.jar
rm -f "../${EXAM_ID}.tar.gz"
COPYFILE_DISABLE=1 tar --exclude='._*' -cvzpf "../${EXAM_ID}.tar.gz" esameASM
rm -rf ./esameASM
#mkdir forzip
#mv esameASM ./forzip
#cp ../Makefile ./forzip
#cd forzip
#COPYFILE_DISABLE=1 zip -r "../../${VM_EXAM_ID}.zip" *
#cd ..
#rm -rf ./forzip
