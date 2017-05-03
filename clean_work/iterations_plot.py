import numpy as np
import initial_grid as ig
import grid
import plotheatmap as hplot
import matplotlib.pyplot as plt
import motion as move
grid = grid.grid('roadmap.csv')
carmap = ig.initial_grid(grid,4,10)
hplot.plot(carmap)
plt.show(block=False)
totalflow = []
time = range(10)
for t in range(10):
    carmap, flow = move.motion(grid, carmap, lim=10)
    totalflow.append(flow)
    
plt.figure()   
hplot.plot(carmap)
plt.show(block=False)
plt.figure()
plt.plot(time,totalflow)
plt.show(block = False)