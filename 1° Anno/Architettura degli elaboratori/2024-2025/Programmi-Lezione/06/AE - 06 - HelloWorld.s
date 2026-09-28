.globl main

.data 
	string: .asciz "Hello world!"

.text 
main:
	li a7, 4
	la a0, string

	ecall
