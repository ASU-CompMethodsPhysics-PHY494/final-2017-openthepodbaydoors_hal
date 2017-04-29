d = 4
right = 14
grid = np.genfromtxt('roadmap.csv',delimiter =',')
x,y = road()
car_position = initial_grid()
for k in range(3):
    for n in range(len(x)):
        for j in range(len(grid)):
            if car_position[x[n],j,k] <= (d-car_position[x[n],j+1,k]):
                car_position[x[n],j+1,k] += car_position[x[n],j,k] 
                car_position[x[n],j,k] = 0
            else:
                car_position[x[n],j,k] = car_position[x[n],j,k] + (car_position[x[n],j+1,k]-d)
                car_position[x[n],j+1,k] = d