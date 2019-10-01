import numpy as np
import matplotlib.pyplot as plt

#fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10) = plt.subplots(nrows = 5, ncols = 2, sharex = True)

iters, nones, pairs, twoPairs, threeKinds, houses, fourKinds, straights, flushes, sFlushes, rFlushes = np.loadtxt('probabilites.txt', delimiter = ',', unpack = True, skiprows = 2)

probs = [nones, pairs, twoPairs, threeKinds, houses, fourKinds, straights, flushes, sFlushes, rFlushes]

fig, ax = plt.subplots(nrows = 5, ncols = 2, sharex = True)

ax[0][0].plot(iters, probs[0], 'r')
ax[0][1].plot(iters, probs[1], 'r')
ax[1][0].plot(iters, probs[2], 'r')
ax[1][1].plot(iters, probs[3], 'r')
ax[2][0].plot(iters, probs[4], 'r')
ax[2][1].plot(iters, probs[5], 'r')
ax[3][0].plot(iters, probs[6], 'r')
ax[3][1].plot(iters, probs[7], 'r')
ax[4][0].plot(iters, probs[8], 'r')
ax[4][1].plot(iters, probs[9], 'r')

plt.tight_layout()
fig.ylabel("Number of Hands")
fig.xlabel("Hands dealt")
'''
ax1.plot(iters, nones, 'r')
ax2.plot(iters, pairs, 'r')
ax3.plot(iters, twoPairs, 'r')
ax4.plot(iters, threeKinds, 'r')
ax5.plot(iters, houses, 'r')
ax6.plot(iters, fourKinds, 'r')
ax7.plot(iters, straights, 'r')
ax8.plot(iters, flushes, 'r')
ax9.plot(iters, sFlushes, 'r')
ax10.plot(iters, rFlushes, 'r')
'''
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
