RARS:=java -jar ./rars1_6.jar
# max number of instructions allowed 305900 (10 x 30590)
JTIMEOUT:=305900

## CSS to decorate HTML
CSS="<style> .my-pre{\
line-height:1.2em;\
background:linear-gradient(180deg,\#ccc 0,\#ccc 1.2em,\#eee 0);\
background-size:2.4em 2.4em;\
background-origin:content-box;\
padding:0 20px;\
text-align:justify;\
width:600px;\
font-family:calibri,arial,sans-serif;} </style>"

TESTS=$(sort $(wildcard test-*.in))
PASSEDFN:=$(TESTS:.in=.pass)

all: $(PASSEDFN) test_results.html


test_results.html: clean check_registration program01.asm Makefile
	@echo $(CSS) > $@
	@echo "<H1>[AE] Test results</H1>" >> $@
	make $(PASSEDFN) | tee -a $@

program01.comp: program01.asm
	@echo "> Compile test</br>"
	@echo
	@rm -f program01.*comp ; \
	$(RARS) a me ae1 nc program01.asm > program01.comp 2> program01.noncomp ; \
	if [ -s program01.noncomp ] ; then  \
		rm -f program01.comp ; \
		echo "COMPILATION FAILED!\n" ; \
		false; \
	else \
		rm -f program01.noncomp ; \
	fi

test-%.out: program01.comp  test-%.in
	@echo "> Running"
	@echo $@ for at most $(JTIMEOUT) instructions
	@F=$(basename $@ .out) ; \
	$(RARS) $(JTIMEOUT) se1 me nc ic program01.asm < $$F.in > $@ 2> $$F.err || cat $$F.err


test-%.pass: test-%.out test-%.expt
	@echo '<pre class="my-pre">'
	@echo Checking $^
	@F=$(basename $@ .pass) ; \
	rm -f $$F*pass ; \
	if (diff -yabBw $^ > $$F.diff ) ; then \
		echo "<span style=\"color:green\">PASSED</span>" ; \
		touch $$F.pass ; \
		max_value=$$(cat "max-iter.expt") ; \
		last_line=$$(tail -n 1 $$F.err) ; \
		if [ "$$last_line" -lt "$$max_value" ]; then \
			echo Run $${last_line} instructions. "<span style=\"color:green\">Eligible for bonus</span>" ; \
			touch $$F.bonus ; \
		else \
			echo Run $${last_line} instructions. Not eligible for bonus as limit is $${max_value} ; \
		fi ; \
	else \
        paste $^ | sed 's/\t/\t\t\t\t\t\t/g' > $$F.paste ; \
		echo "<span style=\"color:red\">NOT PASSED</span><code>" ; \
		touch $$F.nopass ; \
		echo "<div style=\"display: flex; justify-content: space-between;\"><p style=\"margin: 0;\">RISULTATO OTTENUTO</p><p style=\"margin: 0;\">RISULTATO ATTESO</p></div>" ; \
		echo "<div style=\"display: flex; justify-content: space-between;\"><p style=\"margin: 0;\">$$(cat $<)</p><p style=\"margin: 0;\">$$(cat $(word 2,$^))</p></div>" ; \
		echo "</code>" ; \
		last_line=$$(tail -n 1 $$F.err) ; \
		if [ "$$last_line" -ge $(JTIMEOUT) ]; then \
			echo Run $${last_line} instructions. "<span style=\"color:red\">Infinite loop?</span>" ; \
		fi ; \
	fi ; \
	rm -f test*.paste ; \
	rm -f test*.diff
	@echo '</pre>'

printerr:
	cat *err

clean:
	rm -f *.out *.diff *.paste *.pass *.nopass *.bonus *.comp *.nocomp *.err test_results.html

check_registration:
	@if ! grep -q "^# Matricola:\s*[0-9]\+" program01.asm; then \
		echo "Error: No number found after '# Matricola:'" | tee -a test_results.html; \
		exit 1; \
	fi


.PRECIOUS: test-%.out *.out *.err *.diff
