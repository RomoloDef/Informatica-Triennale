.data
N: .word 0x6369616f # I put 'o'=0x6f as first byte
N2: .byte 0x63,0x69,0x61,0x6f
N3: .byte 'c','i','a','o'
N4: .asciz "ciao"

.text

la a0,N
lb x11, 0(a0)   # this contains 0x6f='o'
lb x12, 1(a0) 	# this 3 ...
lb x13, 2(a0)
lb x14, 3(a0)

lw x15,N

la a0, N2
lb x16, 0(a0)   # this contains ?
lb x17, 1(a0) 
lb x18, 2(a0)
lb x19, 3(a0)

la a0, N3
lb x20, 0(a0)   # 
lb x21, 1(a0) 	# 
lb x22, 2(a0)
lb x23, 3(a0)

la a0, N4
lb x24, 0(a0)   # 
lb x25, 1(a0) 
lb x26, 2(a0)
lb x27, 3(a0)
