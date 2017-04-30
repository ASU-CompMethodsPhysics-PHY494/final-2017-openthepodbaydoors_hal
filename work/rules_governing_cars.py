# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 21:43:06 2017

@author: MSmith
"""

import numpy as np
import random

   
grid = np.genfromtxt('roadmap.csv',delimiter =',')


def road(grid):
    #function that creates a value from excel .csv file for both
    #x and y directions that can later be used to create our streets
    x , y = grid.shape
    hor = []
    vert = []
    for i in range(x):
        if grid[i,0] == 1:
            hor.append(i)
    for j in range(y):
        if grid[0,j] == 1:
            vert.append(j)
    return hor, vert
        
    
def initial_grid(d = 4):
    #takes our info from excel .csv file and using 'road' function
    #then spits out some info/does stuff:
        #identifies where cars can and can't be on grid based on excel input
        #gives random assignment of cars on locations that are 'roads' 
            #and not in places we've chosen to be obstructions
        #stores the number of cars in each position
    car_position = np.zeros((len(grid),len(grid),4))
    x , y = road(grid)
    for k in range(4):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i,j] == 0:
                    car_position[i,j] = 0
        else:
            for n in range(len(x)):
                for j in range(len(grid)):
                    car_position[x[n],j,0] = random.randint(0,d)
                    car_position[x[n],j,1] = random.randint(0,d)
            for m in range(len(y)):
                for i in range(len(grid)):
                    car_position[i,y[m],3] = random.randint(0,d)
                    car_position[i,y[m],2] = random.randint(0,d)
    return car_position
    

d = 4

def car_loop_x( point, point_max_value, i ):
    
    #attempt at making function that moves car values no further than
    #grid size and loops around to zero when at edge
    x,y = road(grid)
    number_of_cars = initial_grid()    
    for n in number_of_cars[i]:
        if number_of_cars[i] == 15:
            return number_of_cars[0]
    return number_of_cars 
"""
def east_movement(starting_step, next_step):
    #taking care of the movement problem
    #should take initial placement func and spit out step moves
    x,y = road(grid)
    print("x", x)
    print("y", y)
    number_of_cars = initial_grid()
    print("number of cars", number_of_cars)
    for n in range(len(x)):
            print("len(x)", len(x))
            for j in range(len(grid)):
                print("len(grid)", len(grid))
                starting_step = number_of_cars[x[n],j,k]
                if number_of_cars[x[n],j+1,k] < d:
                    starting_step = d-number_of_cars[x[n],j+1,k]
                    number_of_cars[x[n],j+1,k] += number_of_cars[x[n],j,k] 
                    number_of_cars[x[n],j,k] = 0
                else:
                    number_of_cars[x[n],j,k] = number_of_cars[x[n],j,k] + (number_of_cars[x[n],j+1,k]-d)
                    number_of_cars[x[n],j+1,k] = d
    return number_of_cars
    
    
    for i in number_of_cars[i,j,k]:
        starting_step = initial_grid()
        next_step_east = starting_step[i+1,j,k,1]
    return next_step_east
"""
    
"""    
def north_movement(starting_step, next_step):
    #taking care of the movement problem
    #should take initial placement func and spit out step moves
    for i in car_position[i,j,1]:
        starting_step = initial_grid()
    return next_step_north    
    
def south_movement(starting_step, next_step):
    #taking care of the movement problem
    #should take initial placement func and spit out step moves
    for i in car_position[i,j,2]:
        starting_step = initial_grid()
    return next_step_south

def west_movement(starting_step, next_step):
    #taking care of the movement problem
    #should take initial placement func and spit out step moves
    for i in car_position[i,j,3]:
        starting_step = initial_grid()
    return next_step_west
"""    
    
def simulation():
    #attempt at simulating movement of our cars outside intersections
    x,y = road(grid)
    number_of_cars = initial_grid()
    for k in range(3):
        for n in range(len(x)):
            print("len(x)", len(x))
            for j in range(len(grid)):
                print("len(grid)", len(grid))
                if number_of_cars[x[n],j+1,k] == 0:
                    number_of_cars[x[n],j+1,k] = number_of_cars[x[n],j,k]
                    number_of_cars[x[n],j,k] = 0
                if number_of_cars[x[n],j+1,k] == d:
                    number_of_cars[x[n],j,k] = number_of_cars[x[n],j,k]
                else:
                    if number_of_cars[x[n],j+1,k] > 0 and number_of_cars[x[n],j+1,k] < d:
                        if (number_of_cars[x[n],j,k]) + (number_of_cars[x[n],j,k]) <= d:
                            number_of_cars[x[n],j+1,k] += number_of_cars[x[n],j,k]
                            number_of_cars[x[n],j,k] = 0
                        else:
                            enroute = 0
                            enroute = (d - number_of_cars[x[n],j+1,k])
                            number_of_cars[x[n],j+1,k] += enroute
                            number_of_cars[x[n],j,k] -= enroute
    return number_of_cars
    
beep = simulation()
print("beep", beep)