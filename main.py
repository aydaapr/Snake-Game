from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)



screen.listen()
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)




game_is_on=True

while game_is_on:


  
  
  screen.update()
  time.sleep(0.2)

  snake.move()


 
  

  if snake.head.distance(food)<15:
    food.refresh()
    scoreboard.increase_score()
    snake.extend()
    

  if snake.head.xcor()>290 or snake.head.ycor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290:
    scoreboard.reset()
    snake.reset()
    #game_is_on=False
    #scoreboard.game_over()
    


  for seg in snake.segments[1:]:
    if seg.distance(snake.head)<10:
      scoreboard.reset()
      snake.reset()
      #game_is_on=False
      #scoreboard.game_over() 















screen.exitonclick()