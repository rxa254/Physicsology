#!/usr/bin/env python

from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

[tt, v] = np.loadtxt('data.txt',unpack=True)

plt.figure(figsize=(11,6))
plt.semilogy(tt, v, linestyle='', marker='o', markersize=9, mfc='Blue')

plt.grid(True)
plt.xlabel(r"Time [y]")
plt.ylabel('Ether Velocity UL [km/s]')

plt.title("Ether Velocity Limits over the Years")

plt.savefig("EtherUls.pdf", bbox_inches='tight')
#plt.show()
