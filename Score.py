from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.gamescore= 0
      self.highscore=self.readhighScore()
      self.color("pink")
      self.penup()
      self.hideturtle()
      self.goto(0,290)
      self.updateboard()
      
    def readhighScore(self):
      with open("data.txt",'r') as file:
        self.val = file.read()
      return int(self.val)

       
    def updatehighScore(self):
        with open("data.txt",'w') as file:
          file.write(str(self.highscore))
          
    #printing the score
    def updateboard(self):
        self.clear()
        self.write(f"Score: {self.gamescore}  High Score: {self.highscore}", align="center", font=("Arial", 10, "normal"))
  

    #updating the score increased by 1
    def updatescore(self):
       self.gamescore+=1
       self.updateboard()
    
    def reset(self):
      if self.gamescore > self.highscore:
          self.highscore = self.gamescore
          self.updatehighScore()
      self.gamescore=0
      self.updateboard()