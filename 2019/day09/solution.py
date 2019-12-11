import collections

mem = None
with open('day9.txt') as f:
    mem = [int(i) for i in f.read().strip().split(',')]
    mem = {i: mem[i] for i in range(len(mem))}
    mem = collections.defaultdict(int, mem)
#print(mem)

def computer(i, Q):
    ptr = 0
    offset = 0
    while ptr < len(mem):
        opcode = mem[ptr]
        m1, m2, m3 = opcode//100%10, opcode//1000%10, opcode//10000%10
        p1, p2, p3 = mem[(ptr+1)], mem[(ptr+2)], mem[(ptr+3)]
        v1 = mem[p1+offset] if m1 == 2 else p1 if m1 else mem[p1] if p1 in mem else None
        v2 = mem[p2+offset] if m2 == 2 else p2 if m2 else mem[p2] if p2 in mem else None
        v3 = mem[p3+offset] if m3 == 2 else p3 if m3 else mem[p3] if p3 in mem else None

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
            #Q[(i+1)%5].append(v1)
            print(v1)
            ptr+=2
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
            break
    
Q = [[2]]   # 1 for part1
print(computer(0, Q))

# import itertools

# max_val = -9999999
# for seq in itertools.permutations(range(5)):
#     Q = [[] for _ in range(5)]

#     for i, j in zip(range(5), seq):
#         Q[i].append(j)

#     Q[0].append(0)
#     print(Q)
#     for i in range(5):
#         res = computer(i, Q)
#         max_val = max(max_val, res)

# print(max_val)