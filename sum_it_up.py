##import the modules
import random
import turtle
import result
import os


##create a new class called displayResult
class displayResult:
    def __init__(self, digit):
        self.digit = digit
    def displayTurtle(self,turtle):      #Turtle show!
        if self.digit == 0:              #to display digit number 0
            for i in range(2):
                turtle.forward(100)
                turtle.right(90)
                turtle.forward(200)
                turtle.right(90)
            turtle.forward(100)
        if self.digit == 1:              #to display digit number 1
            turtle.penup()
            turtle.forward(100)
            turtle.right(90)
            turtle.pendown()
            turtle.forward(200)
        if self.digit == 2:              #to display digit number 2
            for i in range(2):
                turtle.forward(100)
                turtle.right(90)
            for j in range(2):
                turtle.forward(100)
                turtle.left(90)
            turtle.forward(100)
        if self.digit == 3:              #to display digit number 3
            for i in range(2):
                turtle.forward(100)
                turtle.right(90)
            turtle.forward(100)
            turtle.forward(-100)
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
        if self.digit == 4:              #to display digit number 4
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(150)
            turtle.forward(-50)
            turtle.left(90)
            turtle.forward(100)
            turtle.forward(-200)
        if self.digit == 5:              #to display digit number 5
            turtle.forward(100)
            turtle.forward(-100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            for i in range(2):
                turtle.right(90)
                turtle.forward(100)
        if self.digit == 6:              #to display digit number 6
            turtle.forward(100)
            turtle.forward(-100)
            turtle.right(90)
            turtle.forward(200)
            for i in range(3):
                turtle.left(90)
                turtle.forward(100)
        if self.digit == 7:              #to display digit number 7
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(200)
        if self.digit == 8:              #to display digit number 8
            turtle.penup()
            turtle.right(90)
            turtle.forward(100)
            turtle.pendown()
            for i in range(3):
                turtle.forward(-100)
                turtle.right(90)
            for i in range(3):
                turtle.forward(-100)
                turtle.left(90)
            turtle.forward(-100)
        if self.digit == 9:              #to display digit number 9
            turtle.penup()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.pendown()
            for i in range(4):
                turtle.left(90)
                turtle.forward(100)
            for i in range(2):
                turtle.right(90)
                turtle.forward(100)

##declare a function for the game section 'Sum It Up'
def start(f_team):
    os.system('cls')
    rng = random.Random()                    #make a random number generator
    SUM = []
    num_record = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    for turn in range(4):                    #play for 4 turns
        i = 0
        for team in f_team:
            print("{0} Round {1} !".format(team.team_name, turn+1))
            start = input("Press 'Enter' to throw the dice")
            dice_throw = rng.randrange(1,7)  #return a random number in range 1-6
            ##print out the number of each turn
            print("The number of {0} for round {1} is {2}".format(team.team_name, turn+1, dice_throw))

            num_record[i][turn] = dice_throw
            i+=1
        print("*********************************************")
    print(num_record)
    i = 0
    for team in f_team:
        SUM.append(sum(num_record[i]))       #sum up the total for each team
        print("Sum of number for team", team.team_name, "=", SUM[i])
        wn = turtle.Screen()                 #create a playground for turtles
        wn.bgcolor("black")                  #set the window background color to black
        wn.title("THE RESULT SESSION")       #set the window title
        dig1 = turtle.Turtle()               #create a turtle, assign to dig1
        dig1.color("DarkGoldenrod1")         #set the turtle color to DarkGoldenrod1
        dig1.pensize(18)                     #set the turtle size to 18
        dig2 = dig1.clone()                  #create a turtle 'dig2' by cloning the characteristic of the turtle 'dig1'

        ##set the initial position of the turtles
        dig1.penup()
        dig1.goto(-175,100)
        dig1.pendown()
        dig2.penup()
        dig2.goto(0,100)
        dig2.pendown()

        if SUM[i] < 10:                      #display result when SUM < 10
            res1 = displayResult(0)          #create an instance of the class
            res1.displayTurtle(dig1)         #display the 1st digit '0'
            res2 = displayResult(SUM[i])     #create another instance of the class
            res2.displayTurtle(dig2)         #display the 2nd digit in range 0-9
        elif 10 <= SUM[i] < 20:              #display result when 10 <= SUM < 20
            res1 = displayResult(1)
            res1.displayTurtle(dig1)
            res2 = displayResult(SUM[i]-10)
            res2.displayTurtle(dig2)
        elif SUM[i] >= 20:                   #display result when SUM >= 20
            res1 = displayResult(2)
            res1.displayTurtle(dig1)
            res2 = displayResult(SUM[i]-20)
            res2.displayTurtle(dig2)
        wn.clear()
        i+=1

    for i in f_team:
        i.score += SUM[f_team.index(i)]
        print(i.team_name, "score:", i.score)
    print("You have to close the windows yourself to continue... 🙂")
    wn.exitonclick()                            #wait for user to close the window
    next_game(f_team)

def next_game(f_team): #method to next module
    os.system('cls')
    result.sorting_result(f_team)

