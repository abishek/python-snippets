import itertools
import enchant

d1 = enchant.Dict("en_UK")
d2 = enchant.Dict("en_US")
l = 'football'
wl = {}
for i in range(3, len(l)+1) :
	for each in itertools.permutations(l, i) :
		w = ''.join(each)
		if d1.check(w) or d2.check(w) :
			wl[w] = None

print len(wl.keys())
print wl.keys()			
