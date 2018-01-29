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
        self.speed = speed
        self.turnDelay = 0 + turnDelay

    def getX(self):
        return self.turt.xcor()
    


    def getY(self):
        return self.turt.ycor()


        
    def forward(self, distance):
        """Moves the turtle forward speed + distance"""
        self.turt.forward(1)

    def turnRight(self, degrees):
        self.turt.right(degrees)
        time.sleep(self.turnDelay)

    def turnLeft(self, degrees):
        self.turt.left(degrees)
        sleep(self.turnDelay)



racerone = RacingTurtle( 0, 0, "Racer one")
eugene = RacingTurtle(15, 0.5, "Eugene 'the machine' Topps")
blaze = RacingTurtle(40, 1, "Blaize")
Zeus = 

eugene.turt.penup()
eugene.turt.sety( 50)
eugene.turt.pendown()

blaze.turt.penup()
blaze.turt.sety( -150)
blaze.turt.pendown()

time.clock()
eugeneStartTime = time.clock()

def runRace(rt):
    time.clock()
    startTime = timw.clock()
    

    #forward 27
    #right 90
    #forward 100
    leg1Distance = 100* (1 - rt.speed/100)

    for i in range(leg1distance):
        rt.forward()
        rt.turnright(90)

        leg2distance = 100 * (1 - rt.speed/100)
    for i in range(leg1distance):
        rt.forward()
        rt.turnright(90)
        rt.forward(100)
        endTime = time.clock()

for runForward(dist, rt):
    distance = int(1 - rt.speed/100)
for i in range(distance):
        rt.forward()
###leg 1
##
##while ( racerone.getX() < 100):
##        racerone.forward(1)
##
###turn
##racerone.turnRight(90)
##
###leg 2
##while ( racerone.getY() < 100):
##        racerone.forward(1)
##receroneStartTime = time.clock()




##
###leg 1
##
##while ( eugene.getX() < 100):
##        eugene.forward(1)
##
###turn
##eugene.turnRight(90)
##
##
###leg 2
##while ( eugene.getY() < 100):
##        eugene.forward(1)
##eugeneStartTime = time.clock()

###leg 1
##
##while ( blaze.getX() < 27):
##        blaze.forward(1)
##
###turn
##blaze.turnRight(90)
##
##
###leg 2
##while ( blaze.getY() < -100):
##        blaze.forward(1)
##blazeStartTime = time.clock()

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
