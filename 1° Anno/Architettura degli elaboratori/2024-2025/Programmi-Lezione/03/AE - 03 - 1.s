.globl main
# (b - c) + (d - e)
# (4 - 3) + (9 - 4)

.data

.text

main:
 	 
	addi s1,zero,4
	addi s2,zero,3
	addi s3,zero,9
	addi s4,zero,4

	sub t0,s1,s2
	sub t1,s3,s4
	add s0,t0,t1


