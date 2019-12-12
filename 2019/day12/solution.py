import numpy

data = [[-6,12,9,-1], [2,-14,5,-4], [-9,-4,-6,9]]
vel = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def get_1000(pos, vel):
    count = 0
    while count < 1000:
        count+=1
        for i in range(len(vel)):
            for j in range(len(vel)):
                if i != j:
                    vel[i] += 1 if pos[j] > pos[i] else -1 if pos[j] < pos[i] else 0
        for i in range(len(pos)):
            pos[i] += vel[i]

for i, j in zip(data, vel):
    get_1000(i,j)
    
res = 0
for i in range(4):
    res += sum(abs(data[j][i]) for j in range(3)) * sum(abs(vel[j][i]) for j in range(3))
print(res)

def get_repeat(pos, vel):
    count = 0
    orig = (pos.copy(), vel.copy())
    while True:
        count+=1
        for i in range(len(vel)):
            for j in range(len(vel)):
                if i != j:
                    vel[i] += 1 if pos[j] > pos[i] else -1 if pos[j] < pos[i] else 0
        for i in range(len(pos)):
            pos[i] += vel[i]
        if orig == (pos, vel):
            break
    return count

res = []
for i, j in zip(data, vel):
    res.append(get_repeat(i, j))

print(numpy.lcm.reduce(res))

