.data
N: .word 0x01020304
N2: .byte 1,2,3,4

.text

la a0, N
lb t0, 0(a0)   # this contains 4
lb t1, 1(a0)   # this 3 ...
lb t2, 2(a0)
lb t3, 3(a0)

lw t4, N 	# 0x01020304


la a0, N2
lb s0, 0(a0)   # this contains 1
lb s1, 1(a0)   # this 2 ...
lb s2, 2(a0)
lb s3, 3(a0)

lw s4, N2 	# 0x04030201
