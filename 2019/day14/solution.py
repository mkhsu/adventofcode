data = None
_from = None
_to = None
with open('day14.txt') as f:
    data = f.readlines()
    _from = [None]*len(data)
    _to = [None]*len(data)
    
for i in range(len(data)):
    data[i] = data[i].strip().split('=>')
    _from[i] = data[i][0].strip().split(',')
    _from[i] = [i.strip().split(' ') for i in _from[i]]
    _from[i] = [[int(i[0]), i[1]] for i in _from[i]]
    _to[i] = data[i][1].strip().split(' ')
    _to[i][0] = int(_to[i][0])

assert(len(_to) == len(set(map(lambda x:x[1], _to))))

import collections
import math

adjlist = collections.defaultdict(list)

leftover = collections.defaultdict(int)

# setup adjlist with to => from
for i in range(len(data)):
    adjlist[_to[i][1]].append(_to[i][0])
    adjlist[_to[i][1]].append(_from[i])

def get_ore(i, item):
    if item == 'ORE':
        return i
    elif i <= leftover[item]:   # no need to make more
        leftover[item] -= i
        return 0
    i -= leftover[item]         # use leftover first
    ore = 0
    unit, pairs = adjlist[item]
    copies = math.ceil(i/unit)   # integer multiple
    for num, from_item in pairs:    # (#X, ABCD)
        ore += get_ore(num * copies, from_item)
    leftover[item] = unit * copies - i   # num made - num wanted
    return ore

print(get_ore(1, 'FUEL'))


want = 1000000000000

i = 0
j = want
while i <= j:
    mid = i + (j-i) // 2
    print('trying:',mid)
    ore = get_ore(mid, 'FUEL')
    print(ore)
    if ore == want:
        break
    if ore > want:
        j = mid-1
    else:
        i = mid+1
