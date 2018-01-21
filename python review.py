#racing turtles

import turtle 
import time
##
##mack = Turtle()
##mack.forward(100)
##mack.left(30)
##mack.forward(100)

#create a stimulation that predicts what turtle will win a race
#Racerone
#Eugene - eugene runs 15%faster than an average turtle, but must wait half a second whenever he turns
#Blaze - retired, but turns at 40% increased speed

class RacingTurtle:

    def __init__ (self, speed, turnDelay, name):
        self.name = name
        self.turt = turtle.Turtle()
        self.speed = 20 * ( 1 + (speed/100))
        self.turnDelay = 0 + turnDelay

    def getX(self):
        return self.turt.xcor()
    


    def getY(self):
        return self.turt.ycor()


        
    def forward(self, distance):
        """Moves the turtle forward speed + distance"""
        self.turt.forward(distance * self.speed)

    def turnRight(self, degrees):
        self.turt.right(degrees)
        sleep(self.turnDelay)

    def turnLeft(self, degrees):
        self.turt.left(degrees)
        sleep(self.turnDelay)



racerone = RacingTurtle( 0, 0, "Racer one")
eugene = RacingTurtle(15, 500, "Eugene 'the machine' Topps")

eugene.turt.penup()
eugene.turt.sety( 50)
eugene.turt.pendown()


time.clock()
eugeneStartTime = time.clock()

#leg 1

while ( racerone.getX() < 100):
        racerone.forward(1)

#turn
racerone.turnright(90)

#leg 2
while ( racerone.getY() < 100):
        recerone.forward(1)
receroneStartTime = time.clock()

#leg 1

while ( eugene.getX() < 100):
        eugene.forward(1)

#turn
eugene.turnright(90)


#leg 2
while ( eugene.getY() < 100):
        eugene.forward(1)
eugeneStartTime = time.clock()

##while True:
##    racerone.forward(1)
##    eugene.forward(1)
##
##    
##    
##
##    if racerone.turt.xcor() > 100:
##        print (racerone.name, "wins!")
##        break
##
##    if eugene.turt.xcor() > 100:
##        print (racerone.name, "wins!")
##        break
