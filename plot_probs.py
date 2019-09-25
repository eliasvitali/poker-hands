import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex = True)

iters, nones, pairs, twoPairs, threeKinds, houses, fourKinds, straights, flushes, sFlushes, rFlushes = np.loadtxt('probabilites.txt', delimiter = ',', unpack = True, skiprows = 2)

ax1.plot(iters, nones, 'r')
ax2.plot(iters, pairs, 'r')
ax3.plot(iters, twoPairs, 'r')
ax4.plot(iters, threeKinds, 'r')

plt.savefig('cards.png', dpi = 250)
'''
#plt.plot(iters, straights, 'r', label = 'Actual')
#plt.plot(iters, straights_th, 'b', label = 'Theoretical')
plt.legend(loc = 'upper right')
plt.xlabel('Iterations')
plt.ylabel('Number of straights')
plt.title("Straights")
plt.savefig('straights.png', dpi = 300)
plt.show()
'''
