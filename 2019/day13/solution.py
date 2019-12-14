import collections
import time

mem = None
with open('day13.txt') as f:
    mem = [int(i) for i in f.read().strip().split(',')]
    mem = {i: mem[i] for i in range(len(mem))}
    mem = collections.defaultdict(int, mem)
assert(mem)

def computer(i, Q, ptrs, offsets):
    ptr = ptrs[i]
    offset = offsets[i]
    while ptr < len(mem):
        opcode = mem[ptr]

        m1, m2, m3 = opcode//100%10, opcode//1000%10, opcode//10000%10
        p1, p2, p3 = mem[(ptr+1)], mem[(ptr+2)], mem[(ptr+3)]

        v1 = mem[p1+offset] if m1 == 2 else p1 if m1 else mem[p1]
        v2 = mem[p2+offset] if m2 == 2 else p2 if m2 else mem[p2]
        v3 = mem[p3+offset] if m3 == 2 else p3 if m3 else mem[p3]

        opcode %= 100
        
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
            ptrs[i] = ptr+2
            offsets[i] = offset
            return v1
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
            return None

d = [' ', 'X', 'O', '=', 'B']
def print_grid(grid):
    print(''.join(grid), flush=True)

grid = ['']*(26*41-1)
for i in range(25):
    grid[i*41+40] = '\n'
Q = [[]]
offsets = [0]
ptrs = [0]
mem[0] = 2  # comment out for part1
p_x = 0
score = 0
fps_goal = 1/90
while True:
    val1 = computer(0, Q, ptrs, offsets)
    if val1 is None:
        break
    val2 = computer(0, Q, ptrs, offsets)
    val3 = computer(0, Q, ptrs, offsets)

    if val3 == 3:
        p_x = val1

    elif val3 == 4:
        Q[0].append(0 if val1 == p_x else 1 if val1 > p_x else -1)

    if val1 == -1 and val2 == 0:
        score = val3
    else:
        grid[val2*41+val1] = d[val3]

    # print('\n\n\n\n\t\t ',score,sep='')
    # print_grid(grid)
    # time.sleep(fps_goal)

print(score)


print(grid.count('O'))
