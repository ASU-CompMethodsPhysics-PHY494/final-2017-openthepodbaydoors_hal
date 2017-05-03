import numpy as np
import intersection as inter
import neighbors as nbr
def motion(grid, carmap, lim):
    dir_ = {'n': 2,
        'e': 0,
        's': 3,
        'w': 1}
    cm = carmap
    new_m = np.zeros_like(cm)
    new_m[:] = cm[:]
    trafficflow = []
    
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            n = nbr.neighbors(cm, i, j)
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
                        else:
                            new_m[current] -= move
                            new_m[new] += move
                if inter.is_intersection(grid,i,j):
                    trafficflow.append(cm[current]-new_m[current])
    intersectiontotal = sum(trafficflow)
            
    return new_m, intersectiontotal