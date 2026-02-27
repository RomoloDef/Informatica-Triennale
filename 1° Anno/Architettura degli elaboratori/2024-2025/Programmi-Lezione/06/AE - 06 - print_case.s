.globl print_string, read_int, print_rez, print_char, exit

.data
	# Syscall lookup table
	print_s: 		.byte 4
	print_i: 		.byte 1
	read_i: 		.byte 5
	print_c: 		.byte 11
	exit_s: 		.byte 10
	
.text	
print_string:                	         # cenno a una procedura
	lb a7, print_s          # print a string (4 means that)
	ecall
	jr ra
	
print_rez:
	lb a7, print_i          # print an integer (1 means that but now is encoded in the lookup table)
	ecall
	jr ra

read_int:
	lb a7, read_i
	ecall
	jr ra

print_char:
	lb a7, print_c
	ecall
	jr ra
	
exit:
	lb a7, exit_s           # Very important: tells the OS to exit the pro
	ecall                   # if we do not add this we may go in infinite loop
