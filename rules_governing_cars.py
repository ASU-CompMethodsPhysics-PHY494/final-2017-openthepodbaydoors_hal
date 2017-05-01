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
                    car_position[x[n],j,0] = random.randint(0,d) #east
                    car_position[x[n],j,1] = random.randint(0,d) #west
            for m in range(len(y)):
                for i in range(len(grid)):
                    car_position[i,y[m],3] = random.randint(0,d) #south
                    car_position[i,y[m],2] = random.randint(0,d) #north
    return car_position
    

d = 4
x,y = road(grid)
number_of_cars = initial_grid()    

def is_intersection(grid,i,j):
    #top = grid[i,j+1] == 1
    #bottom = grid[i, j-1] == 1
    #left = grid[i-1,j] == 1
    #right = grid[i+1,j] == 1
    if j == 0:
        top = grid[i,-1] == 1
    else:
        top = grid[i,j-1] == 1
    if j == (grid.shape[1]-1):
        bottom = grid[i,0] == 1
    else:
        bottom = grid[i, j+1] == 1
    if i == 0:
        left = grid[-1,j] == 1
    else:
        left = grid[i-1,j] == 1
    if i == (grid.shape[1]-1):
        right = grid[0,j] == 1
    else:
        right = grid[i+1,j] == 1
    return top and bottom and left and right

        
def take_turns(number_of_cars):
    number_of_cars = number_of_cars - 1
    return number_of_cars
        
    

def simulation_east(Nsteps=50):
    #attempt at simulating movement of our cars outside intersections
    #have conditions that I think will work moves even if we change d. 
    for k in range(1):
        for S in range(Nsteps):
            for n in range(len(x)):
                #print("len(x)", len(x))
                for j in range(len(grid)):
                    #checking for intersection
                    if is_intersection(number_of_cars[x[n],j+1,k]) == False:
                        #trying to get rid of out of bounds index error/wrapping our array:
                        d = d    
                        if number_of_cars[x[n],j,k] == number_of_cars[x[n],14,k]:
                            number_of_cars[x[n],j+1,k] == number_of_cars[x[n],0,k]
                        else:
                            #here's our main move conditions. 0 and d are the boundaries
                            #then our main else statement is about how to sum remainders
                            #without breaking rules. 
                            if number_of_cars[x[n],j+1,k] == 0:
                                number_of_cars[x[n],j+1,k] = number_of_cars[x[n],j,k]
                                number_of_cars[x[n],j,k] = 0
                            if number_of_cars[x[n],j+1,k] == d:
                                number_of_cars[x[n],j,k] = number_of_cars[x[n],j,k]
                            else:
                                #if number of cars anywhere inbetween bounds, then we either
                                #move all of cars from current spot to next spot
                                #or in the else below, we move a partition that can fit, given d
                                if number_of_cars[x[n],j+1,k] > 0 and number_of_cars[x[n],j+1,k] < d:
                                    if (number_of_cars[x[n],j,k]) + (number_of_cars[x[n],j+1,k]) <= d:
                                        number_of_cars[x[n],j+1,k] += number_of_cars[x[n],j,k]
                                        number_of_cars[x[n],j,k] = 0
                                    else:
                                        enroute = 0
                                        enroute = (d - number_of_cars[x[n],j+1,k])
                                        number_of_cars[x[n],j+1,k] += enroute
                                        number_of_cars[x[n],j,k] -= enroute
                    else:
                        total_d = d*2
                        #since our array will never have intersection at a beginning or ending index
                        #first,confirm there is space beyond intersection, otherwise, no need to check intersection 
                        if number_of_cars[x[n],j+2,k] == d:
                            number_of_cars[x[n],j,k] = number_of_cars[x[n],j,k]
                        if number_of_cars[x[n],j+2,k] < d:
                            #north plus south plus east
                            spot_check = [number_of_cars[x[n],j-2,1], number_of_cars[i,y[m],2], number_of_cars[i+2,y[m],3]]
                            for spot in spot_check:
                                count = 0
                                count = count + spot 
                                if count + number_of_cars[x[n],j,k] <= total_d:
                                    if (number_of_cars[x[n],j,k]) + (number_of_cars[x[n],j+2,k]) <=d:
                                        number_of_cars[x[n],j+2,k] += number_of_cars[x[n],j,k]
                                        number_of_cars[x[n],j,k] = 0
                                    else:
                                        enroute2 = 0
                                        enroute2 = (d - number_of_cars[x[n],j+2,k])
                                        number_of_cars[x[n],j+2,k] += enroute2
                                        number_of_cars[x[n],j,k] -= enroute2
                                else: 
                                    take_turns(number_of_cars[x[n],j,k])
                                    number_of_cars[x[n],j+2,k]
    return number_of_cars


    
beep = simulation(50)
print("beep", beep)