# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 14:23:03 2017

@author: MSmith
"""

import numpy as np
import random


"""
def street_map(row, col):
    #attempt at making an array which has all the points in street map
    return np.array( [ (r, c) for r in range(row) for c in range(col) ] )

streetgrid = street_map(3,3)
print(streetgrid)
print(len(streetgrid))

car_position = np.zeros((len(streetgrid),len(streetgrid)))
print(car_position)
"""

def initial_grid(d = 4):
    grid = np.genfromtxt('roadmap.csv',delimiter =',')
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
right = 14
    
    for i in range(20):
        if i > right:
            i = 0
            car_position[7,i+1] = car_position[7,0]
        elif car_position[7,i] <= (d-car_position[7,i+1]):
            car_position[7,i+1] += car_position[7,i] 
            car_position[7,i] = 0
        else:
            car_position[7,i] = car_position[7,i] + (car_position[7,i+1]-d)
            car_position[7,i+1] = d
        print(car_position[7,i])    





x = 4
for k in range(4):
    for i in range(len(streetgrid)):
        for j in range(len(streetgrid)):
            if streetgrid[i,j] == 0:
                car_position[i,j] = 0
            elif streetgrid[i,j] == 1:
                car_position[4,j,0] = random.randint(0,x)
                car_position[7,j,1] = random.randint(0,x)
                car_position[9,j,1] = random.randint(0,x)
                car_position[i,9,3] = random.randint(0,x)
                car_position[4,j,2] = random.randint(0,x)
                car_position[i,4,3] = random.randint(0,x)
                car_position[9,j,0] = random.randint(0,x)
                car_position[i,9,2] = random.randint(0,x)
                
                
d = 4
right = 14
for i in range(20):
    if i > right:
        i = 0
        car_position[7,i+1] = car_position[7,0]
    elif car_position[7,i] <= (d-car_position[7,i+1]):
        car_position[7,i+1] += car_position[7,i] 
        car_position[7,i] = 0
    else:
        car_position[7,i] = car_position[7,i] + (car_position[7,i+1]-d)
        car_position[7,i+1] = d
    print(car_position[7,i])
"""    