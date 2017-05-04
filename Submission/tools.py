import numpy as np
import random
import matplotlib.pyplot as plt
def streetgrid(filename):
    '''imports and creates initial grid from csv file of 1, 0 with 1 being roads'''
    
    return np.genfromtxt(filename,delimiter =',')



def road(grid):
    '''locates the positions of the road on the grid'''
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
    
def initial_grid(grid, lmin, lim):
    '''Randomly places different number of cars on the road based on limit min and limit max'''
    
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
                    car_position[x[n],j,0] = random.randint(lmin,lim)
                    car_position[x[n],j,1] = random.randint(lmin,lim)
            for m in range(len(y)):
                for i in range(len(grid)):
                    car_position[i,y[m],2] = random.randint(lmin,lim)
                    car_position[i,y[m],3] = random.randint(lmin,lim)
    return car_position

def is_intersection(grid,i,j):
    '''Determines if position on the grid is an intersection'''
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
    """ finds the next position in which cars will move
        x = i
        y = j
    """
    directions = {'n':(i-1,j), 'e':(i,j-1), 'w':(i,j+1), 's':(i+1,j)}
    if i <= carmap.shape[0]:
        if i == 0:
            directions['n'] = (carmap.shape[0]-1,j)
        if i >= carmap.shape[0]-1:
            directions['s'] = (0,j)
    else:
        raise ValueError('i is too big!')
    if j <= carmap.shape[1]:
        if j == 0:
            directions['w'] = (i,carmap.shape[1]-1)
        if j >= carmap.shape[0]-1:
            directions['e'] = (i,0)
    else:
        raise ValueError('j is too big!')
    return directions

def motion(grid, carmap, lim):
    '''moves certain number of cars one timesteps and updates each point with changed values'''
    dir_ = {'n': 2,
        'e': 0,
        's': 3,
        'w': 1}
    cm = carmap
    new_m = np.zeros_like(cm)
    new_m[:] = cm[:]
    trafficflow = []
    z = ['n','s','e','w']
    for i in range(cm.shape[0]-1):
        for j in range(cm.shape[1]-1):
            n = neighbors(cm, i, j)
            for k in z:
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
                        else:
                            new_m[current] -= move
                            new_m[new] += move
                if is_intersection(grid,i,j):
                    trafficflow.append(cm[current]-new_m[current])
    intersection_total = sum(trafficflow)
            
    return new_m, intersection_total

def simulation(filename, lower_lim, upper_lim, maxtime):
    '''simulates traffic flow on a streetgrid
    filename: csv file of 1,0 with 1 representing roads
    lower_lim: min number of cars allowed in one space
    upper limit: max number of cars allowed in one space
    maxtime: total number of time cars move'''    

    grid = streetgrid(filename)
    initialcarmap = initial_grid(grid,lower_lim,upper_lim)
    carmap = initialcarmap
    totalflow = []
    time = range(maxtime)
    for t in range(maxtime):

        carmap, flow = motion(grid, carmap, upper_lim)
        totalflow.append(flow)
    return initialcarmap, carmap, np.asarray((totalflow,time))

def hplot(carmap, view=[]):
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
    
def densityplot(initialcarmap, carmap):
    '''plots the initial and final density of streetgrid
    initialcarmap: initial density of cars on grid before moving=3-d array(x,y,z) x,y = streetgrid, z =direction(north,south,east,west)
    carmap: final density of cars on grid before moving=3-d array(x,y,z) x,y = streetgrid, z =direction(north,south,east,west)'''
    plt.figure()   
    hplot(carmap)
    plt.title('Density of Cars on Road after iterations')
    plt.show(block=False)
    plt.figure()
    hplot(initialcarmap)
    plt.title('Initial Density of Cars on Road')
    return plt.show(block = False)

def totalflowplot(totalflow):
    plt.plot(totalflow[1],totalflow[0], 'o-')
    plt.title('Intersection Flow vs Time')
    plt.ylabel('total cars passing through all intersctions')
    plt.xlabel('time')
    return plt.show(block = False)

