.globl main
.data
A:    .word   5
B:    .word   7
C:    .word  12
D:    .word  -8
.text
main:
    lw a0, A             # Load parameters
    lw a1, B
    lw a2, C
    lw a3, D
    
    jal avgOfSquareAbsSub # Call avgOfSquareAbsSub
    
    li a7, 1             # System call: print int
    ecall
    
    li a7, 10            # Exit
    ecall

# function avgOfSquareAbsSub(a0: int, a1: int, a2: int, a3: int): (a0: int)
#   returns ( ( |a0| - |a1| ) ^ 2 + ( |a2| - |a3| ) ^ 2 ) / 2
avgOfSquareAbsSub:
    addi sp, sp, -28     # Move the stack pointer down
    sw ra, 0(sp)         # First: save the return address
    sw fp, 4(sp)         # Save fp
    sw a0, 8(sp)         # Save the parameters that we use locally 
    sw a1, 12(sp)        # (a0-a7 might be changed by nested call so I save them)
    sw a2, 16(sp)        # but no need to restore them at the end
    sw a3, 20(sp)
    sw s1, 24(sp)        # supposed to be preserved after the call
    
    # First call to squareAbsSub with a0, a1 (already set)
    jal squareAbsSub
    mv s1, a0            # Save the temporary result in s1 
    
    # Second call with a2, a3
    lw a0, 16(sp)         # Load a2 into a0
    lw a1, 20(sp)        # Load a3 into a1
    
    jal squareAbsSub
    add a0, s1, a0       # Sum the temporary result directly to a0
    srai a0, a0, 1       # a0 = a0 / 2 (arithmetic right shift by 1)
    
    # Restore saved registers 
    lw s1, 24(sp)
    lw fp, 4(sp)         # Recover fp
    lw ra, 0(sp)         # Recover return address
    addi sp, sp, 28      # Roll the stack pointer back up
    ret                  # Return

# function squareAbsSub(a0: int, a1: int): (a0: int)
#   returns ( |a0| - |a1| ) ^ 2
squareAbsSub:
    addi sp, sp, -4     # Move the stack pointer down
    sw   fp, 0(sp)
    
    # Calculate |a0|
    bge a0, zero, pos_a0 # If a0 >= 0, skip negation
    neg a0, a0           # a0 = -a0 (absolute value)
pos_a0:
    
    # Calculate |a1|
    bge a1, zero, pos_a1 # If a1 >= 0, skip negation
    neg a1, a1           # a1 = -a1 (absolute value)
pos_a1:
    
    sub a0, a0, a1       # a0 = |a0| - |a1|
    mul a0, a0, a0       # a0 = (|a0| - |a1|)^2
    
    # Restore parameters (but don't overwrite return value in a0)
    lw fp, 0(sp)
    addi sp, sp, 4
    ret
