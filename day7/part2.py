mem = None
with open('day7.txt') as f:
    mem = [int(i) for i in f.read().strip().split(',')]
#print(mem)

def computer(i, Q, ptrs):
    ptr = ptrs[i]
    while ptr < len(mem):
        opcode = mem[ptr]
        m1, m2, m3 = opcode//100%10, opcode//1000%10, opcode//10000%10
        p1, p2, p3 = mem[(ptr+1)%len(mem)], mem[(ptr+2)%len(mem)], mem[(ptr+3)%len(mem)]
        v1 = p1 if m1 else (mem[p1] if p1 < len(mem) else None)
        v2 = p2 if m2 else (mem[p2] if p2 < len(mem) else None)
        v3 = p3 if m3 else (mem[p3] if p3 < len(mem) else None)

        opcode %= 100
        
        if opcode == 1:
            mem[p3] = v1+v2
            ptr+=4
        elif opcode == 2:
            mem[p3] = v1*v2
            ptr+=4
        elif opcode == 3:
            mem[p1] = Q[i][0]
            Q[i].pop(0)
            ptr+=2
        elif opcode == 4:
            Q[(i+1)%5].append(v1)
            return v1, ptr+2
            #print(v1)
            #ptr+=2
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
            mem[p3] = 1 if v1 < v2 else 0
            ptr+=4
        elif opcode == 8:
            mem[p3] = 1 if v1 == v2 else 0
            ptr+=4
        elif opcode == 99:
            return None, i
    

import itertools

max_val = -9999999
for seq in itertools.permutations(range(5,10)):
    Q = [[] for _ in range(5)]
    ptrs = [0]*5

    for i, j in zip(range(5), seq):
        Q[i].append(j)

    Q[0].append(0)
    print(Q)

    out = 0
    i = 0
    while True:
        res, ptrs[i] = computer(i, Q, ptrs)
        if not res:
            break
        if i == 4:
            out = res
        i = (i + 1) % 5
    max_val = max(max_val, out)
        

print(max_val)