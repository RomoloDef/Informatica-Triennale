import turtle
class Tarta:
    "funzioni per visualizzare i rettangoli con la turtle"
    def __init__(self,img,W,H,rettangoli, scala=10):
        turtle.colormode(255)
        self.origin = (W//2), (H//2)
        self.scale  = scala
        self.t = t = turtle.Turtle()
        t.speed(0)
        t.pensize(1)
        t.penup()
        t.hideturtle()
        self.draw_rect(0,0,W,H,(0,0,0),False)
        for C,[xm,xM,ym,yM] in rettangoli.items():
            self.draw_rect(xm,ym,xM-xm+1,yM-ym+1,C,False)

    def reset(self):
        self.t.reset()

    def goto(self,x,y, offset=0):
        x0,y0 = self.origin
        self.t.goto((x-x0)*self.scale+offset, -((y-y0)*self.scale+offset))

    def show_position(self,w,h,d,x,y,W,H):
        "disegna i due rettangoli dell'astronave con sportelli"
        print(w,h,d, 'at', x,y)
        self.t.pensize(2)
        self.draw_rect(x-d,y,  w+d+d,h,    (255,0,0),False)
        self.draw_rect(x,  y-d,w,    h+d+d,(0,255,0),False)

    def draw_rect(self,x,y,w,h,C,filled):
        "disegna un rettangolo"
        t = self.t
        s = self.scale
        t.penup()
        t.color(C)
        self.goto(x, y)
        t.pendown()
        t.setheading(-90)
        if filled: t.begin_fill()
        t.forward(h*s-2)
        t.right(-90)
        t.forward(w*s-2)
        t.right(-90)
        t.forward(h*s-2)
        t.right(-90)
        t.forward(w*s-2)
        t.right(-90)
        if filled: t.end_fill()
        t.penup()

    def draw_point(self,x,y,c):
        "disegna un punto"
        t = self.t
        t.penup()
        t.color(c)
        self.goto(x, y, self.scale//2)
        t.pendown()
        t.dot(2)
        t.penup()
