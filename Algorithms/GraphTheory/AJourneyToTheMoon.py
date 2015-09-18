__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/journey-to-the-moon
'''
line1 = input()
numberOfAstronauts = int(line1.split(" ")[0])
numberOfCountries = int(line1.split(" ")[1])

results = []
covered = []
hh = {}
for n in range(numberOfCountries):
    data = input()
    results.append(data.split())
    covered.extend(data.split())

groups = []
for t in results:
    (jthName,kthName) = t
    jthGroup = -1
    kthGroup = -1

    # Just a simple list of hashes with online merging
    for idx,group in enumerate(groups):
        if jthName in group:
            jthGroup = idx
        if kthName in group:
            kthGroup = idx
    if jthGroup == kthGroup:
        if jthGroup == -1: # Implicit: "and kthGroup == -1"
            groups.append(set((jthName,kthName)))
    elif jthGroup != kthGroup:
        if kthGroup == -1:
            # Merge kthName into jthGroup
            groups[jthGroup].add(kthName)
        elif jthGroup == -1:
            # Merge jthName into kthGroup (redundant if naturally-ordered)
            groups[kthGroup].add(jthName)
        else:
            # Merge jthGroup and kthGroup, since we have a connecting pair
            merged = set()
            merged.update(groups[jthGroup])
            merged.update(groups[kthGroup])
            b1 = set(groups[jthGroup])
            b2 = set(groups[kthGroup])
            groups.remove(b1)
            groups.remove(b2)
            #groups.remove(groups[jthGroup])
            #groups.remove(groups[kthGroup])
            #groups.remove(b2)
            groups.append(merged)
#print([list(g) for g in groups])

full = [str(i) for i in range(numberOfAstronauts)]
missing = len(list(set(full).difference(set(covered))))

totes = []#[1 for i in range(missing)]
for s in groups:
    totes.append(len(s))
#print(totes)

money = 0
import itertools
for i in itertools.combinations(totes, 2):
    money += (i[0] * i[1])

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

print(money + sum(totes) * missing + choose(missing, 2))