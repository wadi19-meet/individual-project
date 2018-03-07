from turtle import *
import random
import time
colormode(255)
setup(1280,720)
bgpic("11.gif")
SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2
Running = True
sleep = 0.0077
tracer = 0
# delay(5)
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

Balls = []
Ball1_pos = []
class Ball(Turtle):
	def __init__(self ,x , y, dx, dy, radius,color):

		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
				
		self.dx = dx
		self.dy = dy
		self.right_side = self.xcor() + radius
		self.left_side = self.xcor() - radius
		self.top_side = self.ycor() + radius
		self.bottom_side = self.ycor() - radius
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color ("yellow")
	def move(self , width, height):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		self.left_side = new_x - self.radius
		self.right_side = new_x + self.radius
		self.top_side = new_y + self.radius
		self.bottom_side = new_y -self.radius
		self.goto(new_x,new_y)
		if self.top_side >= height:
			self.dy = -self.dy

		elif self.bottom_side <= -height:
			self.dy = -self.dy

		elif self.right_side >= width:
			self.dx = -self.dx

		elif self.left_side <= -width:
			self.dx = -self.dx
dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DY)
		

Ball1 = Ball(0,0,dx,dy,15,"color")
Balls.append(Ball1)
Ball1_pos.append(Ball1.pos())
def move_ball():
	for i in Balls:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

class Block(Turtle):
	def __init__(self,x ,y ,dx ,dy, width, height,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.right_side = x + height/2
		self.left_side = x - height/2
		self.dx = dx
		self.dy = dy
		self.height = height
		self.width = width
		self.shape("square")
		self.shapesize(width, height)
		# r = random.randint(0,255)
		# g = random.randint(0,255)
		# b = random.randint(0,255)
		self.color(color)

		

Block1 = Block(SCREEN_WIDTH-25,0,0,0,1,6,"red")
Block2 = Block(-SCREEN_WIDTH+25,0,0,0,1,6,"green")
Blocks = [Block1, Block2]

UP_ARROW = "Up"
DOWN_ARROW = "Down"

Block1.right(90)
Block2.right(90)
def b1_up():
	
	Block1.forward(-50)
def b1_down():
	Block1.forward(50)
def b2_up():
	Block2.forward(-50)
def b2_down():
	Block2.forward(50)		

onkey(b1_up,"Up")
onkey(b1_down,"Down")
onkey(b2_up,"w")
onkey(b2_down,"s")

listen()

# def check_collision():
# 	if Ball1.radius() == Block1.width():
# 		Ball1_pos[Ball1.right(180)]

def check_collison():
	ball_x = Ball1.xcor()
	ball_y = Ball1.ycor()
	which_block = 0
	block1_y = Block1.ycor()
	block1_x = Block1.xcor()
	block2_y = Block2.ycor()
	block2_x = Block2.xcor()
	bottom1_edge = block1_y-Block1.height
	top1_edge = block1_y+Block1.height
	bottom2_edge = block2_y-Block2.height
	top2_edge = block2_y+Block2.height


	if(Ball1.left_side < Block1.right_side and Ball1.right_side > Block1.left_side and Ball1.top_side > bottom1_edge and Ball1.bottom_side < top1_edge):
		Ball1.dx = -Ball1.dx
		Ball1.dy = -Ball1.dy
		print("collision")

	if(Ball1.left_side < Block2.right_side and Ball1.right_side > Block2.left_side and Ball1.top_side > bottom2_edge and Ball1.bottom_side < top2_edge):
		Ball1.dx = -0.1
		Ball1.dy = -0.1
		print("collision")
	# if (Ball1.right_side >= Block1.xcor() and Ball1.ycor() >= Block1.ycor()-Block1.height and Ball1.ycor() <= Block1.ycor()+Block1.height ):
	# 	Ball1.dx = - Ball1.dx
	# 	Ball1.dy = - Ball1.dy

	# if (Ball1.left_side >= Block2.xcor() and Ball1.ycor() >= Block2.ycor()-Block1.height and Ball1.ycor() <= Block2.ycor()+Block2.height ):
	# 	Ball1.dx = - Ball1.dx
	# 	Ball1.dy = - Ball1.dy




	# if(ball_x >= block1_x and ball_y > bottom1_edge and ball_y < top1_edge):
	# 	Ball1.dx = -0.1
	# 	Ball1.dy = -0.1
	# 	print ("collision")

	# if(ball_x >= block2_x and ball_y > bottom2_edge and ball_y < top2_edge):
	# 	Ball1.dx = -0.1
	# 	Ball1.dy = -0.1
	# 	print ("collision")




	# ball_y = Ball1.ycor()
	# which_block = 0
	# if(Ball1.left_side > 0):
	# 	block_y = Block1.ycor()
	# 	which_block = 0
	# else:
	# 	block_y = Block2.ycor()
	# 	which_block = 1

	# if(ball_y >= (block_y-6) and ball_y <= (block_y+6) ):
	# 	Ball1.dx = - Ball1.dx
	# 	Ball1.dy = - Ball1.dy
	# 	return True

	# return False
	











while True:
	Ball1.move(SCREEN_WIDTH,SCREEN_HEIGHT)

	#move_ball()
	#Running = check_collison()


mainloop()