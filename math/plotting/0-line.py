#!/usr/bin/env python3
"""Plots y = x^3 as a solid red line graph."""
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(np.arange(0, 11), y, 'r-')
plt.xlim(0, 10)
plt.show()
