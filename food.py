from turtle import Turtle
import random


class Food(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.color("red")
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.speed("fastest")
    self.refresh()

  def refresh(self):
      y_pos=random.randint(-270, +270)
      x_pos=random.randint(-270, +270)
      self.goto(x=x_pos, y=y_pos)



 