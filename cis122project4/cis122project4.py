# CIS 122 Spring 2015
# Cody Jameson
# Project 4 Starter Code

from turtle import *
from random import *

#Problem 0
def sun_and_earth():
	'''
	When the function sun_and_earth is called, draws two circles
	showing the ratio between the diamter of the sun and the earth.
	[none] -> [2 circles]
	'''
	color("yellow", "yellow")
	begin_fill()
	circle(109)
	end_fill()
	penup()
	forward(115)
	color("blue","blue")
	begin_fill()
	pendown()
	circle(1)
	end_fill()
	return #None

#Problem 1(a)
def square(length):
	'''
	[int] -> [square]
	Square takes one paramter (length) and returns a square.
	'''
	forward(length)
	left(90)
	forward(length)
	left(90)
	forward(length)
	left(90)
	forward(length)
	left(90)
	return #None

#Problem 1(b)
def square(length, scolor):
	'''
	[int,color] -> [square, fill]

	Square takes two parameters (length) and returns a square with a filled color.
	'''
	color(scolor, scolor)
	begin_fill()
	forward(length)
	left(90)
	forward(length)
	left(90)
	forward(length)
	left(90)
	forward(length)
	left(90)
	end_fill()
	return #None

#Problem 1(c)
def triangle(length, tcolor):
	'''
	[int,color] -> [square, fill]

	triangle takes two parameters (length) and returns a square with a filled color.
	'''
	color(tcolor, tcolor)
	begin_fill()
	forward(length)
	left(120)
	forward(length)
	left(120)
	forward(length)
	left(120)
	end_fill()
	return #None

#Problem 1(d)
def house():
	'''
	() -> None
	Takes no parameters
	Draws a house with a door.
	'''
	triangle(200,"brown")
	penup()
	right(90)
	pendown()
	square(200,"yellow")
	penup()
	forward(200)
	left(90)
	forward(80)
	pendown()
	square(40,"orange")
	return #None

#Problem 2(a)

#Begin functions for part a
def rover_loc():
	'''
	() - > int
	Return random number for rover location.
	'''
	return randint(-275,275)

def water_content():
	'''
	() - > int
	Return a random number for water content.
	'''
	return randint(1,290)


def temp():
	'''
	() - > int
	Return a random number for temperature. 
	'''
	return randint(-178, 1)
#End functions for part a


#Problem 2(b)
#Begin function for part b
def mars_explore():
	xpos = rover_loc()
	ypos = rover_loc()
	pendown()
	goto(xpos, ypos)
	stamp()
	water = water_content()
	temp1 = temp()
	print xpos, ypos, water, temp1

	
	
	
#End function for part b

def mars_explore_main():
	'''() -> None

    main function for mars_explore:
        set up print and graphical output
        then call mars_explore repeatedly

    data is printed; None value is returned

    >>> mars_explore_main()
    '''
    print("xpos" , "/t", "ypos", "/t", "water", "/t", "temp1")
    reset()
    title("Mars Rover")
    display_color = "blue"
    color(display_color)
    shape('square')
    stamp()   # draw the rover
    mars_explore()
    mars_explore()
    mars_explore()
    mars_explore()
    mars_explore()
    return #none
    








