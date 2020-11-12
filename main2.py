import matplotlib.pyplot as pyplot
from matplotlib import style
import numpy as np
import pandas as pd

# global vars
B = 3.04 * 10**-7
I1 = 1.04
I2 = 2.03

data = pd.read_csv("Physics-Lab-Data-2.csv", sep=",")
# v1 and r1 are for current = 1.04A r1 is squared
# v1 and r2 are for current = 2.03A r2 is squared
data = data[["v2", "r2"]]

# going to use r^2 vs v graph
x, y = data["v2"], data["r2"]
# get max and min to find range for I1
min_y_value = np.min(y)
max_y_value = np.max(y)

min_x_value = np.min(x)
max_x_value = np.max(x)

range = ((max_y_value) - (min_y_value)) / 2

y1 = min_y_value - range
y2 = max_y_value + range

y3 = min_y_value + range
y4 = max_y_value - range

# these values are from the data csv, using them and applying uncertainty
# points 1 & 2 are for the steepest line
point1 = [min_x_value, y1]
point2 = [max_x_value, y2]

# points 3 & 4 are for the shallowest line
point3 = [min_x_value, y3]
point4 = [max_x_value, y4]

# putting points into an array to plot them the lines in to matplotlib
steep_x_values = [point1[0], point2[0]]
steep_y_values = [point1[1], point2[1]]

shallow_x_values = [point3[0], point4[0]]
shallow_y_values = [point3[1], point4[1]]

m, b = np.polyfit(x, y, 1)

# calculating steep slope and shallow slope values to put get range/uncertainty
m_steep = (y2 - y1) / (max_x_value - min_x_value)
m_shallow = (y3 - y4) / (max_x_value - min_x_value)
slope_range = (m_steep - m_shallow) / 2

# calculating electron to mass ratio i have to put 1 / m because the graph is flipped
ratio = (( m) * 10**4) / (B * I2**2)

# putting r^2 and voltage into graph
style.use("grayscale")
pyplot.suptitle('Radius^2 vs. Voltage', fontsize=20)
pyplot.scatter(x, y, color="navy")

# error bar graphs the uncertainty of the r^2
pyplot.errorbar(x, y, yerr=range, fmt='o', ecolor='navy', elinewidth=1, capsize=2)
# plotting slope
pyplot.plot(x, m*x+b, color="green")

# plotting steepest line
pyplot.plot(steep_x_values, steep_y_values, color="blue")

# plotting shallowest line
pyplot.plot(shallow_x_values, shallow_y_values, color="red")

# labels
pyplot.xlabel('Voltage (v)')
pyplot.ylabel('R^2 (cm^2)')
pyplot.show()

# displaying uncertainty and slope and electron to mass ratio
print("Range/Uncertainty for radius: ", range)
print("Slope: ", m)
print("Steepest Slope: ",  m_steep)
print("Shallowest Slope: ", m_shallow)
print("Slope Range/Uncertainty: ", slope_range)
print("electron-to-mass ratio: ", ratio)

