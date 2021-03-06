# -*- coding: utf-8 -*-
"""
Created on Mon May  1 11:10:25 2017

@author: MSmith
"""

import numpy as np
import matplotlib.pyplot as plt
import random


grid = np.genfromtxt('roadmap.csv',delimiter =',')


def road(grid):
    #defines locations of roads on x and y given some grid
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
    
def initial_grid(dmin = 5, dmax = 10):
    #function creating our initial grid
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
                    car_position[x[n],j,0] = random.randint(dmin,dmax)
                    car_position[x[n],j,1] = random.randint(dmin,dmax)
            for m in range(len(y)):
                for i in range(len(grid)):
                    car_position[i,y[m],3] = random.randint(dmin,dmax)
                    car_position[i,y[m],2] = random.randint(dmin,dmax)
    return car_position


carmap = initial_grid()

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

    
    
def neighbors(carmap, i, j):
     #function defining surrounding points based on cardinal direction
     #also ensures that movement wraps when moving beyond edge of grid
     #x = j
     #y = i
    
    directions = {'n':(i-1,j), 'e':(i,j+1), 'w':(i,j-1), 's':(i+1,j)}
    if i == 0:
        directions['n'] = (carmap.shape[0]-1, j)
    if i == carmap.shape[0]-1:
        directions['s'] = (0,j)
    if j == 0:
        directions['w'] = (i,carmap.shape[1]-1)
    if j == carmap.shape[0]-1:
        directions['e'] = (i,0)
    return directions
    
neighbors(carmap, 0,15)

#direction dictionary is dir_
dir_ = {'n': 2,
        'e': 0,
        's': 3,
        'w': 1}

for d in dir_:
    print(d)
    
def motion(carmap, lim=10):
    #moves our cars on the grid
    cm = carmap
    new_m = np.zeros_like(cm)
    new_m[:] = cm[:]
    
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            n = neighbors(cm, i, j)
            for k in dir_:
                current = (i,j, dir_[k])
                new = n[k] + tuple([dir_[k]])
                if not cm[current] == 0:
                    
                    if cm[new] == 0:
                        new_m[new] = cm[current]
                        new_m[current] = 0
                    if cm[new] == lim:
                        new_m[current] = cm[current]
                    else:
                        if cm[new] > 0 and cm[new] < lim:
                            if cm[current] + cm[new] <= lim:
                                new_m[new] += cm[current]
                                new_m[current] = 0
                        else:
                            enroute = 0
                            enroute = (lim - cm[new])
                            new_m[new] += enroute
                            new_m[current] -= enroute
                    
    return new_m

    
def plot(carmap, view=[]):
    if not len(view) ==0:
        dir_ = {'n': 2,
                'e': 0,
                's': 3,
                'w': 1}
        f = np.zeros_like(carmap[:,:,0])
        for l in view:
            f += carmap[:,:,dir_[l]]
        plt.imshow(f)
    else:
        plt.imshow(carmap.sum(axis=2))
    plt.colorbar()
    
plot(carmap)
plt.show()

#for t in range(1):
#    grid = motion(carmap, lim=10)
#plot(grid)
#plt.show()

    



