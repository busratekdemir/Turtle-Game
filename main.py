import turtle
import random

draw = turtle.Screen()
draw.bgcolor("silver")
draw.title("Catch the Turtle")
draw.setup(800, 600)  # Ekran boyutunu belirledik

little_turtle = turtle.Turtle()
little_turtle.shape("turtle")
little_turtle.color("dark green")
little_turtle.shapesize(2, 2)
little_turtle.penup()
little_turtle.speed(0)

# Skor tablosu için panel
panel = turtle.Turtle()
panel.hideturtle()
panel.penup()
panel.goto(0, 260)

# Oyun mesajları için
message_Box = turtle.Turtle()
message_Box.hideturtle()
message_Box.penup()
message_Box.goto(0, 0)

skor = 0
time = 20
over = False
speed_ms = 1100
side = 60


def panel_yaz(metin):
    panel.clear()
    panel.write(metin, align="center", font=("Arial", 16, "bold"))


def panel_update():
    panel_yaz(f"Time: {time} | Score: {skor}")


def rand_pos():
    w = (draw.window_width() // 2) - side
    h = (draw.window_height() // 2) - side - 60

    max_x = min(w, 350)
    max_y = min(h, 200)
    min_x = max(-w, -350)
    min_y = max(-h, -200)

    x = random.randint(min_x, max_x)
    y = random.randint(min_y, max_y)

    return x, y


def hop():
    if over:
        return
    x, y = rand_pos()
    little_turtle.setheading(random.randint(0, 359))
    little_turtle.goto(x, y)

    current_speed = max(speed_ms - (skor * 50), 500)
    draw.ontimer(hop, current_speed)


def hit(x, y):
    global skor, speed_ms
    if over:
        return
    skor += 1
    panel_update()

    little_turtle.onclick(None)
    little_turtle.goto(rand_pos())
    little_turtle.onclick(hit)


def tick():
    global time, over
    if over:
        return
    if time > 0:
        panel_update()
        time -= 1
        draw.ontimer(tick, 1000)
    else:
        over = True
        little_turtle.onclick(None)
        message_Box.clear()
        message_Box.write(f"Time Over!\nScore: {skor}",
                          align="center", font=("Arial", 24, "bold"))
        message_Box.goto(0, -50)
        message_Box.write("Press SPACE to restart",
                          align="center", font=("Arial", 14, "normal"))


def start():
    global skor, time, over, speed_ms
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


message_Box.write("Catch the Turtle!\nPress SPACE to start",
                  align="center", font=("Arial", 18, "bold"))

draw.onkey(start, "space")
draw.listen()
turtle.mainloop()