import turtle

def draw_many_circles(brad, radius):
    for i in range(0,36):
        brad.right(10)
        brad.circle(radius)

def exit_shape(brad):
    brad.right(90)
    brad.forward(350)

def start_turtles():
    window = turtle.Screen()
    window.bgcolor("green")
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.speed(100)
    brad.color("purple")
    draw_many_circles(brad, 100)
    draw_many_circles(brad, 50)
    exit_shape(brad)
    window.exitonclick()
    
start_turtles()
