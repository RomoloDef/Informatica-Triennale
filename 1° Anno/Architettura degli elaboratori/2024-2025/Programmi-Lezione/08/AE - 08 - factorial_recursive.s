.data

N: .word 5
rez: .word 0

.text

lw a0,N
jal factorial
la t0,rez

sw a1,(t0) # save result

mv a0,a1
li a7,1
ecall

li a7,10 #exit
ecall

factorial: # factorial(a0: int) : (a1: int) return the factorial of a0
	beqz a0,BaseCase
	
	RecursiveStep: # a0 * factorial(a0-1)
		addi sp,sp,-8
		sw ra,0(sp)
		sw a0,4(sp) # qui ci serve salvare a0 perché non siamo foglia
		
		addi a0,a0,-1
		jal factorial # from here all the recursive calls are done and
			      #	the stack is filled, then from the last call each
                              # multiplication is done recovering the value from
                              # the stack. After execution, the result is in a1,
                              # the original a0 is in the stack.
		
		lw   a0,4(sp)
		lw   ra,0(sp)
		addi sp,sp,8
		
		mul a1,a1,a0 

		jr ra

BaseCase:
	li a1,1 # 0! is 1 by definition
	ret	

