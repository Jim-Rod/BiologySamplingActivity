# Create an A1 sized plot with random dots.
# to be used as exercise for y11 Biology
# topic: sampling techniques.

# Whith thanks to http://matplotlib.org/examples/lines_bars_and_markers/scatter_with_legend.html
# and http://www.labri.fr/perso/nrougier/teaching/matplotlib/
# and https://twitter.com/timl

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

X_MAX = 10
Y_MAX = 10

# Make figure aprox A1 size
plt.figure(figsize=(33,23), dpi=80)
plt.xlim(0, X_MAX)
plt.ylim(0, Y_MAX)
plt.ymin, plt.ymax = 0, Y_MAX

# Make the data
data = [('green', 1000, 100, 0.5, 'none'),
        ('blue', 1000, 100, 0.5, 'none'),
        ('red', 500, 200, 1, 'black')]

for (color, n, scale, alpha, edgecolors) in data:
    x, y = rand(2, n)
    x *= X_MAX
    y *= Y_MAX
    s = scale * rand(n)
    plt.scatter(x, y, c=color, s=s, label=color,
                alpha=alpha, edgecolors=edgecolors)

# Set up the grid etc
plt.legend()
plt.grid(False)
plt.xticks(np.arange(0, X_MAX, 0.5))
plt.yticks(np.arange(0, Y_MAX, 0.5))

# save it
plt.savefig('plot.pdf', bbox_inches='tight')
