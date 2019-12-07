mem = None
with open('day5.txt') as f:
    mem = [int(i) for i in f.read().strip().split(',')]
print(mem)

i = 0
while i < len(mem):
    opcode = mem[i]
    m1, m2, m3 = opcode//100%10, opcode//1000%10, opcode//10000%10
    p1, p2, p3 = mem[(i+1)%len(mem)], mem[(i+2)%len(mem)], mem[(i+3)%len(mem)]
    v1 = p1 if m1 else (mem[p1] if p1 < len(mem) else None)
    v2 = p2 if m2 else (mem[p2] if p2 < len(mem) else None)
    v3 = p3 if m3 else (mem[p3] if p3 < len(mem) else None)

    opcode %= 100
    
    if opcode == 1:
        mem[p3] = v1+v2
        i+=4
    elif opcode == 2:
        mem[p3] = v1*v2
        i+=4
    elif opcode == 3:
        mem[p1] = int(input())
        i+=2
    elif opcode == 4:
        print(v1)
        i+=2
    elif opcode == 5:
        if v1 != 0:
            i=v2
        else:
            i+=3
    elif opcode == 6:
        if v1 == 0:
            i=v2
        else:
            i+=3
    elif opcode == 7:
        mem[p3] = 1 if v1 < v2 else 0
        i+=4
    elif opcode == 8:
        mem[p3] = 1 if v1 == v2 else 0
        i+=4
    elif opcode == 99:
        break
    