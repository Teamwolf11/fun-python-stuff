#simple pong game by Mike
# by Mike 
# part 1

import turtle

window = turtle.Screen()
window.title("Pong by @MikeCui")
window.bgcolor("black")
window.setup(width=800,height=600  )
window.tracer(0)





# paddle a
paddleA= turtle.Turtle()
paddleA.speed(0)#speed of animation is set to max
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)


#paddle b
paddleB= turtle.Turtle()
paddleB.speed(0)#speed of animation is set to max
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)


#Ball
ball= turtle.Turtle()
ball.speed(0)#speed of animation is set to max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Function
def paddle_a_up():




#main game loop
while True:
  window.update()





