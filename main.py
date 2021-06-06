from turtle import Turtle,Screen
from paadle import Paddle
from ball import Ball
import time
from score import Scoreboard
screen=Screen()
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()  
score=Scoreboard()  
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
#Detect the collision with wall
    if  ball.ycor() >280 or ball.ycor()<-280:
        ball.bounce_y()
   #Detect collision with right paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    #if r_paddle misses the ball
    if ball.xcor()>380 :
        ball.reset_position()
        score.l_point()
 #if l_paddle misses the ball
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()