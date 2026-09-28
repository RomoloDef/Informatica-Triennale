.data 
	Array: .word 10, 20, 23, 30, 1, 10
.text 
	addi t0, zero, 6
	la t1, Array
	addi s7, t1, 24
	
While: 	#while (i < N){
   bge t1, s7, WhileEnd # IF i >= N THEN jump to WhileEnd
   lw t2, (t1)		#Load Array[i];	
   add s0, s0, t2 	# s = s + Array[i];
   addi t1, t1, 4	# i +=1;
   j While		#}
WhileEnd:
