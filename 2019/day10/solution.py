grid = None
with open('day10.txt') as f:
    grid = f.readlines()
    assert(len(grid) == 25)
    grid = [line.strip() for line in grid]

# print(grid)
for row in grid:
    assert(len(row) == 25)

# no longer used after discovering atan2
# def computeGCD(x, y): 
  
#    while(y): 
#        x, y = y, x % y 
  
#    return x 

import collections
import math


max_angles = {}
max_val = 0
mi,mj = 0,0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            angles = collections.defaultdict(list)
            s = set()
            for k in range(len(grid)):
                for l in range(len(grid[k])):
                    if i == k and j == l:
                        continue
                    if grid[k][l] == '#':
                        dy, dx = k-i, l-j
                        # gcd = computeGCD(abs(dy), abs(dx))
                        angles[math.atan2(dy,dx)+(math.pi)].append((dy,dx)) # from 0 to pi*2 radians
            if len(angles) > max_val:
                mi,mj = i,j
            max_angles = angles.copy() if len(angles) > max_val else max_angles
            max_val = max(len(angles), max_val)
print('max num of angles:',max_val)
print('at:', mi, mj)

k = sorted(max_angles.keys())
i = k.index(math.pi/2)
j = 0
last_vap_i, last_vap_j = 0,0
while j < 200:
    while len(max_angles[k[i]]) == 0:
        i = (i+1) % len(k)
    mind = 99999
    for v,w in max_angles[k[i]]:
        mind = min(abs(v) + abs(w), mind)
    for v,w in max_angles[k[i]]:
        if abs(v)+abs(w) == mind:
            last_vap_i, last_vap_j = v+mi, w+mj
            max_angles[k[i]].remove((v,w))
            break
    i = (i+1) % len(k)
    j+=1
print('200th vaporized:', last_vap_i, last_vap_j)
