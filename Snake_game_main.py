import turtle as t
from snake import MySnake
from Food import Food
from Score import Scoreboard
import time

#screen initialization
gamescreen=t.Screen()
gamescreen.bgcolor("black")
gamescreen.title("Hungry Rio")
gamescreen.tracer(0)

#creating the snake,food and score object
snake=MySnake()
food=Food()
score=Scoreboard()

#choose the head direction
gamescreen.listen()
gamescreen.onkey(snake.up,"Up")
gamescreen.onkey(snake.down,"Down")
gamescreen.onkey(snake.left,"Left")
gamescreen.onkey(snake.right,"Right")

#let the game begin
game_is_on=True
while game_is_on:

    gamescreen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.updatescore()
        snake.extend()

    #collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
        score.reset()
        snake.start()
    
    #collision with tail
    for s in snake.snake[1:]:
        if snake.head.distance(s)<10:
           score.reset()
           snake.start()  

gamescreen.exitonclick()