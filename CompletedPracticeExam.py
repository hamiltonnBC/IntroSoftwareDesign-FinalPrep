######################################################################
# Created by Nicholas Hamilton, with inspiration from the Berea College Computer Science Department
# Date: 04/17/2024


######################################################################
# Author:  Nicholas Hamilton
# Username: Hamiltonn
#
# Assignment: CODING FINAL PRACTICE EXAM
# Instructions:
# CREATE MULTIPLE OBJECTS FROM A CLASS SCRIPT
# TODO ONLY VIEW THIS FILE AFTER ATTEMPTING THE PRACTICE EXAM
#
########################################################################

import turtle

class House:
    def __init__(self, color="blue", x=0, y=0, size=1):
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.turt = turtle.Turtle()
        self.turt.speed(5)  # You can make this zero to save time

    def draw_rectangle(self, width, height, color): #DO NOT EDIT THIS FUNCTION
        """Draws the base of the house."""
        self.turt.penup()
        self.turt.goto(self.x, self.y)
        self.turt.pendown()
        self.turt.fillcolor(color)
        self.turt.begin_fill()
        for i in range(2):
            self.turt.forward(width * self.size)
            self.turt.right(90)
            self.turt.forward(height * self.size)
            self.turt.right(90)
        self.turt.end_fill()

    def draw_roof(self, width): #DO NOT EDIT THIS FUNCTION
        """Draws the roof of the house."""
        roof_height = width * 0.5
        self.turt.penup()
        self.turt.goto(self.x, self.y)
        self.turt.pendown()
        self.turt.fillcolor("darkred")
        self.turt.begin_fill()
        self.turt.forward(width * self.size)
        self.turt.left(135)
        self.turt.forward(roof_height * self.size * 1.414)
        self.turt.left(90)
        self.turt.forward(roof_height * self.size * 1.414)
        self.turt.left(135)
        self.turt.end_fill()

    def draw_house(self): #DO NOT EDIT THIS FUNCTION
        """Draws the entire house."""
        base_width = 100
        base_height = 80
        self.draw_rectangle(base_width, base_height, self.color)
        self.draw_roof(base_width)


def main():
    wn = turtle.Screen()  # Set up the window
    wn.title("House Drawing")

    # Draw the first house with default attributes
    house1 = House()
    house1.draw_house()

    # Draw a red house, smaller and shifted left
    house2 = House(color="red", x=-200, y=-50, size=0.75)
    house2.draw_house()

    # Draw a large green house, shifted right
    house3 = House(color="green", x=200, y=-50, size=1.5)
    house3.draw_house()

    wn.exitonclick()  # Wait for a user click to close the window

main()
