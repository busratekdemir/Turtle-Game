import turtle
import random

draw = turtle.Screen()
draw.bgcolor("silver")
draw.title("Cath the Turtle")

little_turtle = turtle.Turtle()
little_turtle.shape("turtle")
little_turtle.color("dark green")
little_turtle.shapesize(2, 2)
little_turtle.penup()
little_turtle.speed(0)

#skor tablosu için panel
panel=turtle.Turtle()
panel.hideturtle()
panel.penup()
panel.goto(0,260)

#oyun mesajları için
message_Box=turtle.Turtle()
message_Box.hideturtle()
message_Box.penup()
message_Box.goto(0,20)

skor=0
time=20
over= False
speed_ms=1100 #yer değiştirme hızı
side=40

def panel_yaz(metin):
    panel.clear()
    panel.write(metin, align="center",font=("Arial",12,"bold"))

def panel_update():
    panel_yaz(f"Time: {time} Skor: {skor}")


#kaplumbağa ekran içinde rastgele yerlere konumlara yerleşebilmeli
def rand_pos():
    w = draw.window_width() //2 -side # yarı genişlikten kenar payını düştük
    h = draw.window_height() //2 -side #aynı şekilde yükseklik
    return random.randint(-w,w), random.randint(-h,h)

def hop():
    if over: #over True dönerse çalışmayı bırakacak
        return
    x,y = rand_pos() # rand_pos fonksiyonu çağırdık
    little_turtle.setheading(random.randint(0,359))
    little_turtle.goto(x,y)
    draw.ontimer(hop,speed_ms)

def hit(x,y):
    global skor, speed_ms
    if over: return
    skor +=1
    panel_update()
    little_turtle.onclick(None)
    hop()
    little_turtle.onclick(hit)

def tick():
    global time,over
    if over: return
    if time >0:
        panel_update()
        time = time-1
        draw.ontimer(tick,1000) #1sn sonra geri çağırır
    else:
        over = True
        little_turtle.onclick(None)
        message_Box.clear()
        message_Box.write(f"Time over! \nSkor: {skor}",align="center",font=("Arial",28,"bold"))

def start():
    global skor, time, over,speed_ms
    skor = 0
    time = 20
    over = False
    speed_ms = 1100
    panel_update()
    message_Box.clear()
    little_turtle.goto(rand_pos())
    little_turtle.onclick(hit)
    hop()
    tick()

draw.onkey(start,"space")
draw.listen()
start()
turtle.mainloop()