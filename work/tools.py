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

grid = np.genfromtxt('roadmap_with_intersections.csv',delimiter =',')


""" This function is supposed to say if a point in the grid is an intersection or not"""

def is_intersection(grid,i,j):
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

"""list of intersections locations"""
def grid_int(grid):
    intersections  = []
    for n in range(grid.shape[0]):
        for m in range(grid.shape[1]):
            if is_intersection(grid, n, m):
                intersections.append((n,m))
    return  np.asarray(intersections)


carmap = initial_grid(4)

def neighbors(carmap, i, j):
    """ x = j
        y = i
    """
    directions = {'n':(i-1,j), 'e':(i,j+1), 'w':(i,j-1), 's':(i+1,j)}
    if i == 0:
        directions['n'] = (i, carmap.shape[0]-1)
    if i == carmap.shape[0]-1:
        directions['s'] = (0,j)
    if j == 0:
        directions['w'] = (i,carmap.shape[1]-1)
    if j == carmap.shape[0]-1:
        directions['e'] = (i,0)
    return directions

"""find neighbors of intersections"""    

def neighbors_int(grid):
    ni=[]
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if is_intersection(grid, i,j):
                ni.append(neighbors(grid, i,j))
    return ni


""" define direction dictionary as dir"""

dir_ = {'n': 2,
        'e': 0,
        's': 3,
        'w': 1}
        
"""get cars moving"""

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
                if not cm[current] == 0:
                    cars = cm[current]
                    if cm[new] < lim:
                        move = cars // 2
                        res = lim - cm[new] - move
                        if res < 0:
                            new_m[current] -= lim - move
                            new_m[new] += lim - move
                    
    return new_m 

"""Plot 'heatmap' of cars"""

def plot(grid, view=[]):
    if not len(view) == 0:
        dir_dict = {'n': 0,
                    'e': 1,
                    'w': 2,
                    's':3}
        f = np.zeros_like(grid[:,:,0])
        for d in view:
            f += grid[:,:,dir_dict[d]]
        plt.imshow(f)
    else:
        plt.imshow(grid.sum(axis=2),cmap='hot')
    plt.colorbar()

