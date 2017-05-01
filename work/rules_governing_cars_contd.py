# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 21:43:06 2017

@author: MSmith
"""

import numpy as np
import random
k_north = 0
k_south = 1
k_east = 2
k_west = 3
   
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
            #print("hor", hor)
    for j in range(y):
        if grid[0,j] == 1:
            vert.append(j)
            #print("vert", vert)
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
                            car_position[x[n],j,0] = random.randint(0,d) #north
                            car_position[x[n],j,1] = random.randint(0,d) #south
                    for m in range(len(y)):
                        for i in range(len(grid)):
                            car_position[i,y[m],3] = random.randint(0,d) #west
                            car_position[i,y[m],2] = random.randint(0,d) #east
    return car_position
    

"""
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

for n in range(grid.shape[0]):
    #print(grid.shape[0])
    for m in range(grid.shape[1]):
        #print(grid.shape[1])
        if is_intersection(grid, n, m):
            intersection_array[n,m] = 1

#list of intersections locations
intersections = []
for n in range(grid.shape[0]):
    for m in range(grid.shape[1]):
        if is_intersection(grid, n, m):
            intersections.append((n,m))
print("intersections", intersections)           

"""   


d = 4
number_of_cars = initial_grid()    

"""
def simulation_north(Nsteps=50):
    #attempt at simulating movement of our cars outside intersections
    #have conditions that I think will work moves even if we change  d. 
    x,y = road(grid)
    print("x", x)
    print("y", y)
    number_of_cars = initial_grid()
    #for k in range(1):
    for S in range(Nsteps):
        for n in x:
            for g in range(len(grid)):
                #here's our main move conditions. 0 and d are the boundaries
                #then our main else statement is about how to sum remainders
                #without breaking rules. 
                            if number_of_cars[x[n],j+1] == 0:
                                number_of_cars[x[n],j+1] = number_of_cars[x[n],j]
                                number_of_cars[x[n],j] = 0
                            if number_of_cars[x[n],j+1] == d:
                                number_of_cars[x[n],j] = number_of_cars[x[n],j]
                            else:
                                
                                #if number of cars anywhere inbetween bounds, then we either
                                #move all of cars from current spot to next spot
                                #or in the else below, we move a partition that can fit, given d
                                if number_of_cars[x[n],j+1] > 0 and number_of_cars[x[n],j+1] < d:
                                    if (number_of_cars[x[n],j]) + (number_of_cars[x[n],j+1]) <= d:
                                        number_of_cars[x[n],j+1] += number_of_cars[x[n],j]
                                        number_of_cars[x[n],j] = 0
                                    else:
                                        enroute = 0
                                        enroute = (d - number_of_cars[x[n],j+1])
                                        number_of_cars[x[n],j+1] += enroute
                                        number_of_cars[x[n],j] -= enroute
    return number_of_cars

                 #else:
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
                           """         
    


    

def how_many_cars_here(x, y, z):
    howmany = int(number_of_cars[x][y][z])
    return howmany
        
alex 









#we should have tests for the functions to make sure they are working. 

#Alex function list(then simple, don't need intersection mumbo)
#1) How many cars at x,y,z(direction)? 
#2) Can add car at x,y,z(direction)? query's map at that location, make sure traffic moving in correct direction, and 
    #max value not hit
#3) Remove car from location x,y,z(direction). 
#4) Then i would have another function that adds car from location x,y,z(direction)
"""
for x = 0, x< map size x:
    for y = 0, y< map size y:
        for direction in k_north, k_south, east, west:
            if Number_of_cars_function(how many cars at a point at x,y,direction) > 0:
                UpdatelocationFunction( to find new location.) 
                Can_add_car_at_new_x_y_directionFunction(checks for maximum space is available)
                    then remove car current x, current y
                    add car new x, new y to new spot
                    
                
                
                    UpdateLocationFunction (which takes original x and y and direction and return new x and new y)
                    if og x and y are 0 and og direction is k-east, then incriment x by 1, 
                    if k-south, then incriemtn that way:
                        but then check to see if you're off edge of the map
                        if x = 14
                            x = 0
                        or something like if y = -1, then y = 0
            
""" 