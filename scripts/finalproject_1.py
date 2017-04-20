# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:26:35 2017

@author: ASmith
"""
import numpy as np
import random
#import time
#import os
#import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns

"""
#this is attempt at car position
def CarStart(position):
    for i in streets[]:
        for j in streets[i][]:
            z = streets[i][j][]
    if z = 0:
        position = random.location()
    return position
"""


"""
#Attempt to give car's ability to move
def CarMove(init_position, new_position, step):
    
    return new_position

    
"""
    
    
    
    
"""    
State = type("State", tuple, {})
class NorthCar(State):
    def moveNorth(position):
        position += 1
        print("The North Car Moved!")
        return position
        
class EastCar(State):
    def moveEast(position):
        position += 1
        print("The East Car Movied!")
        return position
        
"""

def street_map(row, col):
    
    #attempt at making an array which has all the points in street map
    return np.array( [ (r, c) for r in range(row) for c in range(col) ] )

def car_step_moves( point, point_max_value, ):
    
    #attempt at making function that moves cars one point at a time
    # point - just a point on x or y axis
    # point_max_value - the maximum value along x or y axis 
    # returns - either a wrap-around movement or progresses one point
        

    if point == point_max_value:
        return 0
    else:
        return point + 1
        

#print(x)    
streetgrid = street_map(100,100)
#print(streetgrid)

x = random.randint(0, 99)
y = random.randint(0, 99)
print('x ', x)
print('y ', y)
initial_northbound_position = x
initial_eastbound_position = y
print('initial north pos ' , initial_northbound_position)
print('initial east pos ' , initial_eastbound_position)

start_point_northbound = ([x])
print('start point northbound', start_point_northbound)
locations_north = []
locations_north.append(start_point_northbound)
print('locations north array ', locations_north)

start_point_eastbound = ([y])
print('start point eastbound', start_point_eastbound)
locations_east = []
locations_east.append(start_point_eastbound)
print('locations east array ', locations_east)

#working on defining motion for north car
for i in range(5):
    new_north_coord = car_step_moves(initial_northbound_position, 100)
    initial_northbound_position = new_north_coord
    locations_north.append([new_north_coord])
    #print('new_north_coord ', new_north_coord)

    
#working on defining motion for east car    
for i in range(5):
    new_east_coord = car_step_moves(initial_eastbound_position, 100)
    initial_eastbound_position = new_east_coord
    locations_east.append([new_east_coord])
    #print('new_east_coord ', new_east_coord)
    
print('locations north array ', locations_north)
print('locations east array ', locations_east)  




