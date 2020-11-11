import matplotlib.pyplot as pyplot
from matplotlib import style
import numpy as np
import pandas as pd

data = pd.read_csv("Physics-Lab-Data.csv", sep=",")
# v1 and r1 are for current = 1.04A r1 is squared
# v1 and r2 are for current = 2.03A r2 is squared
data = data[["v1", "r1"]]


# going to use r^2 vs v graph
x, y = data["v1"], data["r1"]
# get max and min to find range for I1
min_y_value = np.min(y)
max_y_value = np.max(y)

min_x_value = np.min(x)
max_x_value = np.max(x)

range = ((max_y_value) - (min_y_value)) / 2

# these values are from the data csv, using them and applying uncertainty
# points 1 & 2 are for the steepest line
point1 = [min_x_value, min_y_value - range]
point2 = [max_x_value, max_y_value + range]

# points 3 & 4 are for the shallowest line
point3 = [min_x_value, min_y_value + range]
point4 = [max_x_value, max_y_value - range]

steep_x_values = [point1[0], point2[0]]
steep_y_values = [point1[1], point2[1]]

shallow_x_values = [point3[0], point4[0]]
shallow_y_values = [point3[1], point4[1]]

m, b = np.polyfit(x, y, 1)



print("Range/Uncertainty for Current I = 1.04 A: ", range)
print("Slope: ", m)

# putting r^2 and voltage into graph
style.use("grayscale")
pyplot.suptitle('Radius^2 vs. Voltage', fontsize=20)
pyplot.scatter(x, y, color="navy")

# error bar graphs the uncertainty of the r^2
pyplot.errorbar(x, y, yerr=range, fmt='o', ecolor='navy', elinewidth=1, capsize=2)

# plotting slope/ line of best fit
pyplot.plot(x, m*x+b, color="green")

# plotting steepest line
pyplot.plot(steep_x_values, steep_y_values, color="blue")

# plotting shallowest line
pyplot.plot(shallow_x_values, shallow_y_values, color="red")

# labels
pyplot.xlabel('Voltage (v)')
pyplot.ylabel('R^2 (cm^2)')
pyplot.show()


