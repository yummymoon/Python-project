import numpy as np
from matplotlib import pyplot as plt

np.random.seed(100)
x = np.linspace(-1, 1, 100).reshape(100, 1)
y = 3*np.power(x, 2) +2