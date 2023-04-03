from turtle import Turtle
ALIGNEMENT="center"
FONT=("Ariel", 20, "normal")

class Scoreboard(Turtle):

  
  def __init__(self):
    super().__init__()
    self.score=0
    file=open("my_file.txt")
    self.highscore=int(file.read())
    file.close()
    self.color("white")
    self.penup()
    self.goto(x=0, y=270)
    self.hideturtle()
    self.update_score()
    
    
  

  def update_score(self):
    self.clear()
    self.write(f"score={self.score}, highscore={self.highscore}", align=ALIGNEMENT, font=FONT)


  #def game_over(self):
    #self.goto(x=0, y=0)
    #self.write("GAME OVER", align=ALIGNEMENT, font=FONT)
    
  def reset(self):
    if self.score>self.highscore:
      self.highscore=self.score
      with open("my_file.txt", mode="w") as file:
        file.write(f"{self.highscore}")
        
        
    self.score=0
    self.update_score()


  def increase_score(self):
    self.score+=1
    self.update_score()

    
    


  
    


    

