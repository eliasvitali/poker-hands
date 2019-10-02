import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def ncr(n, k):
	return comb(n, k, exact = False)

iters, nones, pairs, twoPairs, threeKinds, houses, fourKinds, straights, flushes, sFlushes, rFlushes = np.loadtxt('probabilites.txt', delimiter = ',', unpack = True, skiprows = 2)
iters1, nones1, pairs1, twoPairs1, threeKinds1, houses1, fourKinds1, straights1, flushes1, sFlushes1, rFlushes1 = np.loadtxt('actuals.txt', delimiter = ',', unpack = True, skiprows = 2)

probs = [nones, pairs, twoPairs, threeKinds, houses, fourKinds, straights, flushes, sFlushes, rFlushes]
probs1 = [nones1, pairs1, twoPairs1, threeKinds1, houses1, fourKinds1, straights1, flushes1, sFlushes1, rFlushes1]


freq_tot = ncr(52,5)
rFlush_th = 100*ncr(4,1)/freq_tot
sFlush_th = 100*(ncr(10,1)*ncr(4,1)-ncr(4,1))/freq_tot
fourKind_th = 100*ncr(13,1)*ncr(4,1)*ncr(12,1)/freq_tot
fullHouse_th = 100*ncr(13,1)*ncr(4,3)*ncr(12,1)*ncr(4,2)/freq_tot
flush_th = 100*(ncr(13,5)*ncr(4,1) - ncr(10,1)*ncr(4,1))/freq_tot
straight_th = 100*(ncr(10,1)*(ncr(4,1)**5) - ncr(10,1)*ncr(4,1))/freq_tot
threeKind_th = 100*ncr(13,1)*ncr(4,3)*ncr(12,2)*(ncr(4,1)**2)/freq_tot
twoPair_th = 100*ncr(13,2)*(ncr(4,2)**2)*ncr(11,1)*ncr(4,1)/freq_tot
pair_th = 100*ncr(13,1)*ncr(4,2)*ncr(12,3)*(ncr(4,1)**3)/freq_tot
none_th = 100*((ncr(13,5) - 10)*((ncr(4,1)**5) - 4))/freq_tot

n = float(len(iters1))/100

plt.figure()
plt.plot(iters, probs[0], 'r', label = 'Theoretical: %.6f %%'%(none_th))
plt.plot(iters, probs1[0], 'b', label = 'Actual: %.6f %%'%(probs1[0][-1]/n))
plt.xlabel('# of Hands dealt')
plt.ylabel('# of no-pairs')
plt.title('No Pair')
plt.legend(loc = 'upper left')
plt.savefig('plots/nones.png', dpi = 250)

plt.figure()
plt.plot(iters, probs[1], 'r', label = 'Theoretical: %.6f %%'%(pair_th))
plt.plot(iters, probs1[1], 'b', label = 'Actual: %.6f %%'%(probs1[1][-1]/n))
plt.title('Pair')
plt.xlabel('# of Hands dealt')
plt.ylabel('# of Pairs')
plt.legend(loc = 'upper left')
plt.savefig('plots/pairs.png', dpi = 250)

plt.figure()
plt.plot(iters, probs[2], 'r', label = 'Theoretical: %.6f %%'%(twoPair_th))
plt.plot(iters, probs1[2], 'b', label = 'Actual: %.6f %%'%(probs1[2][-1]/n))
plt.title('Two-Pair')
plt.xlabel('# of Hands dealt')
plt.ylabel('# of Two-Pairs')
plt.legend(loc = 'upper left')
plt.savefig('plots/twoPairs.png', dpi = 250)

plt.figure()
plt.plot(iters, probs[3], 'r', label = 'Theoretical: %.6f %%'%(threeKind_th))
plt.plot(iters, probs1[3], 'b', label = 'Actual: %.6f %%'%(probs1[3][-1]/n))
plt.title('Three-of-a-Kind')
plt.xlabel('# of Hands dealt')
plt.ylabel('# of Three-of-a-Kinds')
plt.legend(loc = 'upper left')
plt.savefig('plots/threeKinds.png', dpi = 250)

plt.figure()
plt.plot(iters, probs[4], 'r', label = 'Theoretical: %.6f %%' %(fullHouse_th))
plt.plot(iters, probs1[4], 'b', label = 'Actual: %.6f %%'%(probs1[4][-1]/n))
plt.title('Full House')
plt.xlabel('# of Hands dealt')
plt.ylabel('# of Full-Houses')
plt.legend(loc = 'upper left')
plt.savefig('plots/houses.png', dpi = 250)

plt.figure()
plt.plot(iters, probs[5], 'r', label = 'Theoretical: %.6f %%' %(fourKind_th))
plt.plot(iters, probs1[5], 'b', label = 'Actual: %.6f %%'%(probs1[5][-1]/n))
plt.title('Four-of-a-Kind')
plt.xlabel('# of Hands dealt')
plt.ylabel('# of Four-of-a-Kinds')
plt.legend(loc = 'upper left')
plt.savefig('plots/fourKinds.png', dpi = 250)

plt.figure()
plt.plot(iters, probs[6], 'r', label = 'Theoretical: %.6f %%'%(straight_th))
plt.plot(iters, probs1[6], 'b', label = 'Actual: %.6f %%'%(probs1[6][-1]/n))
plt.title('Straight')
plt.xlabel('# of Hands dealt')
plt.ylabel('# of Straights')
plt.legend(loc = 'upper left')
plt.savefig('plots/straights.png', dpi = 250)

plt.figure()
plt.plot(iters, probs[7], 'r', label = 'Theoretical: %.8f %%'%(flush_th))
plt.plot(iters, probs1[7], 'b', label = 'Actual: %.8f %%'%(probs1[7][-1]/n))
plt.title('Flush')
plt.xlabel('# of Hands dealt')
plt.ylabel('# of Flushes')
plt.legend(loc = 'upper left')
plt.savefig('plots/flushes.png', dpi = 250)

plt.figure()
plt.plot(iters, probs[8], 'r', label = 'Theoretical: %.9f %%'%(sFlush_th))
plt.plot(iters, probs1[8], 'b', label = 'Actual: %.9f %%'%(probs1[8][-1]/n))
plt.title('Straight Flush')
plt.xlabel('# of Hands dealt')
plt.ylabel('# of Straight Flushes')
plt.legend(loc = 'upper left')
plt.savefig('plots/sFlushes.png', dpi = 250)

plt.figure()
plt.plot(iters, probs[9], 'r', label = 'Theoretical: %.9f %%'%(rFlush_th))
plt.plot(iters, probs1[9], 'b', label = 'Actual: %.9f %%'%(probs1[9][-1]/n))
plt.title('Royal Flush')
plt.xlabel('# of Hands dealt')
plt.ylabel('# of Royal Flushes')
plt.legend(loc = 'upper left')
plt.savefig('plots/rFlushes.png', dpi = 250)
