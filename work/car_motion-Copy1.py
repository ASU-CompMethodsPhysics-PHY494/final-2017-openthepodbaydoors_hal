
# coding: utf-8

# In[5]:

import initial_grid as ig


# In[6]:

carmap = ig.initial_grid(4)


# In[7]:

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


# In[214]:

def neighbors_int(grid):
    ni=[] # neighbors of intersecitons
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if is_intersection(grid, i,j):
                ni.append(neighbors(grid, i,j))
    return ni


# In[209]:

#direction dictionary is dir_
dir_ = {'n': 2,
        'e': 0,
        's': 3,
        'w': 1}


# In[210]:

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


# In[211]:

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

