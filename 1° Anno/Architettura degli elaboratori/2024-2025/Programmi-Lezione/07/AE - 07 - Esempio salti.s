.text

main: li x0,0
beqz x0, hello
addi t1,t1,0
addi t1,t1,0
addi t1,t1,0
addi t1,t1,0
addi t1,t1,0
addi t1,t1,0
addi t1,t1,0
addi t1,t1,0
addi t1,t1,0
addi t1,t1,0
hello: j ok
ok: la t1,main
jr t1