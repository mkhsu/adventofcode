import collections

mem = None
with open('day11.txt') as f:
    mem = [int(i) for i in f.read().strip().split(',')]
    mem = {i: mem[i] for i in range(len(mem))}
    mem = collections.defaultdict(int, mem)
#print(len(mem))
assert(mem)

def computer(i, Q, ptrs, offsets):
    ptr = ptrs[i]
    offset = offsets[i]
    while ptr < len(mem):
        opcode = mem[ptr]
        # print(opcode)
        m1, m2, m3 = opcode//100%10, opcode//1000%10, opcode//10000%10
        p1, p2, p3 = mem[(ptr+1)], mem[(ptr+2)], mem[(ptr+3)]
        # print(opcode,p1,p2,p3)
        v1 = mem[p1+offset] if m1 == 2 else p1 if m1 else mem[p1]
        v2 = mem[p2+offset] if m2 == 2 else p2 if m2 else mem[p2]
        v3 = mem[p3+offset] if m3 == 2 else p3 if m3 else mem[p3]

        opcode %= 100

        # print(opcode,p1,p2,p3)
        # print(v1,v2)
        
        if opcode == 1:
            mem[p3+offset if m3 == 2 else p3] = v1+v2
            ptr+=4
        elif opcode == 2:
            mem[p3+offset if m3 == 2 else p3] = v1*v2
            ptr+=4
        elif opcode == 3:
            mem[p1+offset if m1 == 2 else p1] = Q[i][0]
            Q[i].pop(0)
            ptr+=2
        elif opcode == 4:
            #Q[(i+1)%5].append(v1)
            return v1, ptr+2, offset
        elif opcode == 5:
            if v1 != 0:
                ptr=v2
            else:
                ptr+=3
        elif opcode == 6:
            if v1 == 0:
                ptr=v2
            else:
                ptr+=3
        elif opcode == 7:
            mem[p3+offset if m3 == 2 else p3] = 1 if v1 < v2 else 0
            ptr+=4
        elif opcode == 8:
            mem[p3+offset if m3 == 2 else p3] = 1 if v1 == v2 else 0
            ptr+=4
        elif opcode == 9:
            offset += v1
            ptr+=2
        elif opcode == 99:
            return None, i, offset

d = 0
x, y = 0, 0
grid = collections.defaultdict(str)
grid[(x,y)] = '■'   # '□' for part1
s = set()
Q = [[]]
offsets = [0]
ptrs = [0]
while True:
    Q[0].append(0 if not grid[(x,y)] else (0 if grid[(x,y)] == ' ' else 1))
    val1, ptrs[0], offsets[0] = computer(0, Q, ptrs, offsets)
    if val1 is None:
        break
    val2, ptrs[0], offsets[0] = computer(0, Q, ptrs, offsets)
    if val2 is None:
        break
    s.add((x,y))
    grid[(x,y)] = '■' if val1 == 1 else ' '
    d = (d+4+(-1 if val2 == 0 else 1)) % 4 # 0==up, 1==right, 2==down, 3==left
    if d == 0:
        y += 1
    elif d == 1:
        x += 1
    elif d == 2:
        y -= 1
    elif d == 3:
        x -= 1
    else:
        assert(False)

max_x, min_x = -9999,9999
max_y, min_y = -9999,9999
for (x, y) in grid.keys():
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)

# print(min_x, min_y, max_x, max_y)

for i in range(max_y, min_y - 1, -1):
    for j in range(min_x, max_x + 1):
        print(grid[(j,i)] if grid[(j,i)] else ' ', end='')
    print()
print(len(s))
