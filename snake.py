from turtle import Turtle

POSITIONS=[(0, 0), (-20, 0), (-40, 0)]
DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:

  def __init__(self):
    self.segments=[]
    self.create_snake()
    self.head=self.segments[0]

  def create_snake(self):
    for position in POSITIONS:
      self.create_segment(position)


  def create_segment(self, position):    
      new_turtle=Turtle(shape="square")
      new_turtle.color("white")
      new_turtle.penup()
      new_turtle.goto(position)
      self.segments.append(new_turtle)
      
   
  def reset(self):
    for seg in self.segments:
      seg.goto(1000, 1000)
    self.segments.clear()
    
    self.create_snake()
    self.head=self.segments[0]


  
  def extend(self):
    
    self.create_segment(self.segments[-1].position())
      



  def move(self):
    
    for seg_num in range(len(self.segments)-1, 0, -1):
      new_x=self.segments[seg_num-1].xcor()
      new_y=self.segments[seg_num-1].ycor()

      self.segments[seg_num].goto(x=new_x, y=new_y )
    
    
    self.head.forward(DISTANCE)
 
    
  


  def up(self):   
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
       
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
    
  def right(self):
    
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
    
    

    



  