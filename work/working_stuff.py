# -*- coding: utf-8 -*-
"""
Created on Mon May  1 11:10:25 2017

@author: MSmith
"""

import numpy as np
import matplotlib.pyplot as plt
import random






def road(grid):
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
    
def initial_grid(dmin = 0, dmax = 20):
    
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


carmap = initial_grid(4)

def neighbors(carmap, i, j):
    """ x = j
        y = i
    """
    directions = {'s':(i-1,j), 'e':(i,j+1), 'w':(i,j-1), 'n':(i+1,j)}
    if i == 0:
        directions['s'] = (carmap.shape[0]-1, j)
    if i == carmap.shape[0]-1:
        directions['n'] = (0,j)
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
    
def motion(carmap, lim=5):
    cm = carmap
    new_m = np.zeros_like(cm)
    new_m[:] = cm[:]
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            n = neighbors(cm, i, j)
            for k in dir_:
                current = (i,j, dir_[k])
                new = n[k] + tuple([dir_[k]])
                new2 = n[new[i,j,k]]
                if not cm[current] == 0:
                    if is_intersection == False:
                        if cm[new]== 0:
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
                    else:
                        lim_inton =  lim * 4 // 2
                        for 
                        if cm[new2] == lim:
                            new_m[current] = cm[current]
                        if cm[new2] < lim:
                            #north plus south plus east
                            spot_check = [number_of_cars[x[n],j-2,1], number_of_cars[i,y[m],2], number_of_cars[i+2,y[m],3]]
                            for spot in spot_check:
                                count = 0
                                count = count + spot 
                                if count + cm[current] <= lim_intersection:
                                    if cm[current] + cm[new2] <= lim:
                                        cm[new2] += cm[current]
                                        cm[current] = 0
                                    else:
                                        enroute2 = 0
                                        enroute2 = (lim - cm[new2)
                                        cm[new2] += enroute2
                                        cm[current] -= enroute2
                                else: 
                                    take_turns(cm[current])
                                    cm[new2]
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


#for t in range(5):
#    grid = motion(carmap, lim=10)
#plot(grid)

for t in range(1):
    grid = motion(carmap, lim=10)
    plot(grid)

for t in range(25, 5):
    grid = motion(carmap, lim=10)
    plot(grid)


for t in range(25, 5):
    grid = motion(carmap, lim=10)
    plot(grid)
    

for t in range(25, 5):
    grid = motion(carmap, lim=10)
    plot(grid)

plt.show()
