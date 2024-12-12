from turtle import Turtle 

POSITIONS=[(0,0),(0,-20),(0,-40)]
class MySnake:
   def __init__(self):
      #creating the snake body
      self.snake=[]
      self.create_snake()
      self.head=self.snake[0]

#initializing the snake body parts
   def create_snake(self):
        for p in POSITIONS:
          self.add_segment(p)
         

#adding parts to snake
   def add_segment(self,position):  
      rio=Turtle(shape="square")
      rio.color("white")
      rio.penup()
      rio.goto(position)
      self.snake.append(rio)

#Extending the snake   
   def extend(self):
      self.add_segment(self.snake[-1].position())

#moving the snake
   def move(self):
       for p in range(len(self.snake)-1,0,-1):
         new_x=self.snake[p-1].xcor()
         new_y=self.snake[p-1].ycor()
         self.snake[p].goto(new_x,new_y)
       self.head.forward(15)

#giving the directions
   def up(self):
      if self.head.heading() != 270:
         self.head.setheading(90)
   def down(self):
      if self.head.heading() != 90:
         self.head.setheading(270)
   def right(self):
      if self.head.heading() != 180:
         self.head.setheading(0)
   def left(self):
      if self.head.heading() != 0:
         self.head.setheading(180)      

#starting the snake again for next game
   def start(self):
      for a in self.snake:
         a.goto(1000,1000)
      self.snake.clear()
      self.create_snake()
      self.head=self.snake[0]