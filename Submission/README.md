To run the code:
from final-2017-Openthepodbaydoors hal/Submission import tools.py
Running Simulation:
call simulation function and input the following objects
filename: roadmap.csv
Lower lim: least number of cars allowed in position (should be greater than zero
upper lim: most numbers of cars allowed initially in a position
maxtime: total number of iterations
will return three objects:
- initial number of cars in each position on the street
- final number of cars in each position on the street after iterations
- list of cars that went through the intersection in each iteration

The code is not operating as expected however the initial grid setup works and the simulation updates the positions.

The following plotting functions work appropriately as well

To plot a density map:
Run the simulation such that the return values are identified
call densityplot function for density map of cars and input:
- first object returned from simulation
- second object returned from simulation

call totalflowplot function to plot of flow throuh intersections as a function of iterations and input:
- third object returned in simulation function


