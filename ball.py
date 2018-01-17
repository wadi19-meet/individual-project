from turtle import *
import random
import time

colormode(255)
tracer(0)
hideturtle()


class Ball(Turtle):
	def __init__(self,x ,y ,dx ,dy , color, radius):
		Turtle.__init__(self)
		pu()
		self.goto(x,y)
		self.color = color		
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		randomcolor = ((r,g,b))

	def move(self , width, height):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		left_side = ball1.xcor() - ball1.radius
		Right_side = ball1.xcor() + ball1.radius
		top_side = ball1.ycor() + ball1.radius
		bottom_side = ball1.ycor() -ball1.radius

		if top_side >= height/2:
			self.dy = -self.dy

		elif bottom_side <= -height/2:
			self.dy = -self.dy

		elif right_side >= width/2:
			self.dx = -self.dx

		elif left_side <= -width/2:
			self.dx = -self.dx
	
		self.goto(new_x,new_y)








			