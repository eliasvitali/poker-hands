import random as ran
import time
from scipy.special import comb
import matplotlib.pylab as plt

rank_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
def init_deck():
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ['S', 'D', 'H', 'C']
    deck = []
    for i in range(len(ranks)):
        for j in range(len(suits)):
            deck.append(suits[j]+ranks[i])
    return deck

def is_ordered(ranks):
    return sorted(ranks) == list(range(min(ranks), max(ranks) + 1))

def ncr(n, k):
    return comb(n, k, exact = False)


def is_royalFlush(hand):
    hand_ranks = [i[1] for i in hand]
    ranks_num = [rank_dict[hand_ranks[i]] for i in range(len(hand_ranks))]
    hand_suits = [i[0] for i in hand]
    if(len(list(dict.fromkeys(hand_suits))) == 1 and 'A' in hand_ranks and 'T' in hand_ranks and 'J' in hand_ranks and 'Q' in hand_ranks and 'K' in hand_ranks):
        return True
    else:
        return False

def is_straightFlush(hand):
    hand_ranks = [i[1] for i in hand]
    ranks_num = [rank_dict[hand_ranks[i]] for i in range(len(hand_ranks))]
    hand_suits = [i[0] for i in hand]
    if(len(list(dict.fromkeys(hand_suits))) == 1 and is_ordered(ranks_num)):
        return True
    else:
        return False

def is_fourKind(hand):
    hand_ranks = [i[1] for i in hand]
    ranks_num = [rank_dict[hand_ranks[i]] for i in range(len(hand_ranks))]
    ranks_num = sorted(ranks_num)
    #has to either be 4 cards of same rank + higher unmatched card or 4 cards of same rank + lower unmatched card
    result1 = ranks_num[0] == ranks_num[1] and ranks_num[1] == ranks_num[2] and ranks_num[2] == ranks_num[3]
    result2 = ranks_num[1] == ranks_num[2] and ranks_num[2] == ranks_num[3] and ranks_num[3] == ranks_num[4]
    return (result1 or result2)

def is_fullHouse(hand):
    hand_ranks = [i[1] for i in hand]
    ranks_num = [rank_dict[hand_ranks[i]] for i in range(len(hand_ranks))]
    ranks_num = sorted(ranks_num)
    result1 = ranks_num[0] == ranks_num[1] and ranks_num[1] == ranks_num[2] and ranks_num[3] == ranks_num[4]
    result2 = ranks_num[0] == ranks_num[1] and ranks_num[2] == ranks_num[3] and ranks_num[3] == ranks_num[4]
    return (result1 or result2)


def is_flush(hand):
    hand_suits = [i[0] for i in hand]
    if(len(list(dict.fromkeys(hand_suits))) == 1):
        return True
    else:
        return False

def is_straight(hand):
    hand_ranks = [i[1] for i in hand]
    ranks_num = [rank_dict[hand_ranks[i]] for i in range(len(hand_ranks))]
    if is_ordered(ranks_num):
        return True
    else:
        return False

def is_threeKind(hand):
    hand_ranks = [i[1] for i in hand]
    ranks_num = [rank_dict[hand_ranks[i]] for i in range(len(hand_ranks))]
    ranks_num = sorted(ranks_num)
    result1 = ranks_num[0] == ranks_num[1] and ranks_num[1] == ranks_num[2] and ranks_num[3] != ranks_num[0] and ranks_num[4] != ranks_num[0] and ranks_num[3] != ranks_num[4]
    result2 = ranks_num[1] == ranks_num[2] and ranks_num[2] == ranks_num[3] and ranks_num[0] != ranks_num[1] and ranks_num[0] != ranks_num[4] and ranks_num[4] != ranks_num[1]
    result3 = ranks_num[2] == ranks_num[3] and ranks_num[3] == ranks_num[4] and ranks_num[0] != ranks_num[2] and ranks_num[0] != ranks_num[1] and ranks_num[1] != ranks_num[2]
    return (result1 or result2 or result3)

def is_twoPair(hand):
    hand_ranks = [i[1] for i in hand]
    ranks_num = [rank_dict[hand_ranks[i]] for i in range(len(hand_ranks))]
    ranks_num = sorted(ranks_num)
    result1 = ranks_num[1] == ranks_num[2] and ranks_num[3] == ranks_num[4] and ranks_num[0] != ranks_num[1] and ranks_num[0] != ranks_num[3]
    result2 = ranks_num[0] == ranks_num[1] and ranks_num[3] == ranks_num[4] and ranks_num[2] != ranks_num[0] and ranks_num[2] != ranks_num[3]
    result3 = ranks_num[0] == ranks_num[1] and ranks_num[2] == ranks_num[3] and ranks_num[4] != ranks_num[0] and ranks_num[4] != ranks_num[2]
    return (result1 or result2 or result3)

def is_pair(hand):
    hand_ranks = [i[1] for i in hand]
    ranks_num = [rank_dict[hand_ranks[i]] for i in range(len(hand_ranks))]
    ranks_num = sorted(ranks_num)
    if(is_fourKind(hand) or is_fullHouse(hand) or is_threeKind(hand) or is_twoPair(hand)): return False
    result1 = ranks_num[0] == ranks_num[1]
    result2 = ranks_num[1] == ranks_num[2]
    result3 = ranks_num[2] == ranks_num[3]
    result4 = ranks_num[3] == ranks_num[4]
    return (result1 or result2 or result3 or result4)

num_rFlush = 0
num_sFlush = 0
num_fourKind = 0
num_fullHouse = 0
num_flush = 0
num_straight = 0
num_threeKind = 0
num_twoPair = 0
num_pair = 0
num_none = 0

freq_tot = ncr(52,5)
rFlush_th = ncr(4,1)/freq_tot
sFlush_th = (ncr(10,1)*ncr(4,1)-ncr(4,1))/freq_tot
fourKind_th = ncr(13,1)*ncr(4,1)*ncr(12,1)/freq_tot
fullHouse_th = ncr(13,1)*ncr(4,3)*ncr(12,1)*ncr(4,2)/freq_tot
flush_th = (ncr(13,5)*ncr(4,1) - ncr(10,1)*ncr(4,1))/freq_tot
straight_th = (ncr(10,1)*(ncr(4,1)**5) - ncr(10,1)*ncr(4,1))/freq_tot
threeKind_th = ncr(13,1)*ncr(4,3)*ncr(12,2)*(ncr(4,1)**2)/freq_tot
twoPair_th = ncr(13,2)*(ncr(4,2)**2)*ncr(11,1)*ncr(4,1)/freq_tot
pair_th = ncr(13,1)*ncr(4,2)*ncr(12,3)*(ncr(4,1)**3)/freq_tot
none_th = ((ncr(13,5) - 10)*((ncr(4,1)**5) - 4))/freq_tot

n = 1e6
iters = []
nones = []
nones_th = []
pairs = []
pairs_th = []
twoPairs = []
twoPairs_th = []
threeKinds = []
threeKinds_th = []
flushes = []
flushes_th = []
straights = []
straights_th = []
houses = []
houses_th = []
fourKinds = []
fourKinds_th = []
sFlushes = []
sFlushes_th = []
rFlushes = []
rFlushes_th = []

start = time.clock()

for i in range(int(n)):
    
    hand = ran.sample(init_deck(), 5)

    if is_royalFlush(hand):
        num_rFlush += 1
    
    elif is_straightFlush(hand):
        num_sFlush += 1
    
    elif is_fourKind(hand):
        num_fourKind += 1
    
    elif is_fullHouse(hand):
        num_fullHouse += 1
    
    elif is_flush(hand):
        num_flush += 1
    
    elif is_straight(hand):
        num_straight += 1
    
    elif is_threeKind(hand):
        num_threeKind += 1
    
    elif is_twoPair(hand):
        num_twoPair += 1
    
    elif is_pair(hand):
        num_pair += 1
    
    else:
        num_none += 1
    
    iters.append(float(i))
    nones.append(num_none)
    nones_th.append(float(i)*none_th)
    pairs.append(num_pair)
    pairs_th.append(float(i)*pair_th)
    twoPairs.append(num_twoPair)
    twoPairs_th.append(float(i)*twoPair_th)
    threeKinds.append(num_threeKind)
    threeKinds_th.append(float(i)*threeKind_th)
    houses.append(num_fullHouse)
    houses_th.append(float(i)*fullHouse_th)
    fourKinds.append(num_fourKind)
    fourKinds_th.append(float(i)*fourKind_th)
    flushes.append(num_flush)
    flushes_th.append(float(i)*flush_th)
    straights.append(num_straight)
    straights_th.append(float(i)*straight_th)
    sFlushes.append(num_sFlush)
    sFlushes_th.append(float(i)*sFlush_th)
    rFlushes.append(num_rFlush)
    rFlushes_th.append(float(i)*rFlush_th)

end = time.clock()
proc_t = end - start

prob_rFlush = 100*num_rFlush/float(n)
prob_sFlush = 100*num_sFlush/float(n)
prob_flush = 100*num_flush/float(n)
prob_straight = 100*num_straight/float(n)
prob_fourKind = 100*num_fourKind/float(n)
prob_fullHouse = 100*num_fullHouse/float(n)
prob_threeKind = 100*num_threeKind/float(n)
prob_twoPair = 100*num_twoPair/float(n)
prob_pair = 100*num_pair/float(n)
prob_none = 100*num_none/float(n)

print(f"Dealing {n} hands took {proc_t} seconds!")

print(f"len(iters) = {len(iters)}")

fname = 'probabilites.txt'
with open(fname, 'w') as out_file:
    out_file.write("iters,none,pair,twoPair,threeKind,fullHouse,fourKind,straight,flush,sFlush,rFlush\n")
    for i in range(len(iters)):
	    out_file.write(str(iters[i]) + ',' + str(nones_th[i])+ ',' + str(pairs_th[i]) + ',' + str(twoPairs_th[i]) + ','+str(threeKinds_th[i]) + ',' + str(houses_th[i]) + ',' + str(fourKinds_th[i]) + ',' + str(straights_th[i]) + ',' + str(flushes_th[i]) + ',' + str(sFlushes_th[i]) + ',' + str(rFlushes_th[i]) + '\n')


fname2 = 'actuals.txt'
with open(fname2, 'w') as out_file2:
    out_file2.write("iters,none,pair,twoPair,threeKind,fullHouse,fourKind,straight,flush,sFlush,rFlush\n")
    for i in range(len(iters)):
	    out_file2.write(str(iters[i]) + ',' + str(nones[i])+ ',' + str(pairs[i]) + ',' + str(twoPairs[i]) + ','+str(threeKinds[i]) + ',' + str(houses[i]) + ',' + str(fourKinds[i]) + ',' + str(straights[i]) + ',' + str(flushes[i]) + ',' + str(sFlushes[i]) + ',' + str(rFlushes[i]) + '\n')



print("Done!")
