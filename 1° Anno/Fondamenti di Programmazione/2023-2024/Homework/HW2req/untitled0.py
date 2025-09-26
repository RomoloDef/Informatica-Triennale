#module mux2 #(parameter N=8)
#(
  #input logic [N-1:0] a, b
  #input logic s,
  #output logic [N-1:0] y
#);

#assign y = s? a:b;

#endomodule

#module testebench ();
#input [9:0] d1, d0, out;
#logic s;
#mux2 #(10) dut(.a(d1),.b(d0),.s(s),.y(out));

#initial begin
#$monitor("d1=0x%h, d0=0x%h, y=0x%h, s=%d", d1, d0, s, y)
#s=0;
#d1 = 10'd37
#d0 = 10'h37
#10
#d1 = 1
#10
#s=0
#$finish
#end

#endmodule
#---------------------------------------------------------------
#module mux2 #(parameter N=8)
#(
  #input logic [N-1:0] a, b
  #input logic s,
  #output logic [N-1:0] y
#);

#assign y = s? a:'z;

#assign y = (!s)? a:'z;

#endomodule

#module testebench ();
#input [9:0] d1, d0, out;
#logic s;
#mux2 #(10) dut(.a(d1),.b(d0),.s(s),.y(out));

#initial begin
#$monitor("d1=0x%h, d0=0x%h, y=0x%h, s=%d", d1, d0, s, y)
#s=0;
#d1 = 10'd37
#d0 = 10'h37
#10
#d1 = 1
#10
#s=0
#$finish
#end

#endmodule
#---------------------------------------------------------------
 #module mux2 #(parameter N=8)
 #(
   #input logic [N-1:0] a, b
   #input logic s,
   #output logic [N-1:0] y
 #);
 
#always comb begin : blcokName
#if (s==1) y=b;
#else y=a;
#end

#endmodule
#---------------------------------------------------------------
#module mux4 #(parameter N=8)
 #(
   #input logic [N-1:0] a, b, c, d
   #input logic s,
   #output logic [N-1:0] y
 #);

#always comb begin : blockName
#case(s)
# 2'b00 y=a
# 2'b01 y=b
# 2'b10 y=c
# 2'b11 y=d

#endmodule

#module testebench ();
#input [9:0] d3, d2, d1, d0, out;
#logic s;
#mux2 #(10) dut(.a(d0),.b(d1),.c(d2),.d(d3),.s(s),.y(out));

#initial begin
#$monitor("d3=0x%h, d2=0x%h, d1=0x%h, d0=0x%h, y=0x%h, s=%d", d3, d2, d1, d0, s, y)
#s=0;
#d1 = 10'd37
#d0 = 10'h37
#10
#d1 = 1
#10
#10
#d2 = 1
#10
#d3 = 1
#10
#s=0
#$finish
#end

#endmodule
#------------------------------------------------------------------
#module seven segment
#input logic [3:0] sw,
#output logic [7:0] out
#(
#always comb
#case(sw)
#0: out =7' b1111110
#1: out =7' b0110000
#8: out =7' b1111111
#10: out =7' b 111011
#default: out= 0;
#endcase
#------------------------------------------------------------------
