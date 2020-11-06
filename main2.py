import matplotlib.pyplot as pyplot
from matplotlib import style
import numpy as np
import pandas as pd

data = pd.read_csv("Physics-Lab-Data-2.csv", sep=",")
# v1 and r1 are for current = 1.04A r1 is squared
# v1 and r2 are for current = 2.03A r2 is squared
data = data[["v2", "r2"]]


# going to use r^2 vs v graph
x, y = data["v2"], data["r2"]
# get max and min to find range for I1
min_y_value = np.min(y)
max_y_value = np.max(y)

range_1 = ((max_y_value) - (min_y_value)) / 2

m, b = np.polyfit(x, y, 1)

print("Range/Uncertainty for Current I = 1.04 A: ", range_1)
print("Slope: ", m)

# putting r^2 and voltage into graph
style.use("grayscale")
pyplot.suptitle('Radius^2 vs. Voltage', fontsize=20)
pyplot.scatter(x, y, color="navy")

# error bar graphs the uncertainty of the r^2
pyplot.errorbar(x, y, yerr=range_1, fmt='o', ecolor='navy', elinewidth=1, capsize=2)
# plotting slope
pyplot.plot(x, m*x+b, color="green")
# labels
pyplot.xlabel('Voltage (v)')
pyplot.ylabel('R^2 (cm^2)')
pyplot.show()


