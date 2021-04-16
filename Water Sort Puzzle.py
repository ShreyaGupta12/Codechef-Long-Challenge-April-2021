def disp(N, M, C, D, B, L):
    print(' ' * 33 + '1  2  3  M')
    for i in range(1, N+2+1): print('tube', i, 'upgradeCost=%d' % C[i], 'capacity=%d' % L[i], B[i])
    print()
def main(N, M, C, D, B, L, debug=False):
    ops, cost = [], 0
    if debug: disp(N, M, C, D, B, L)
    while True:
        peeks = {}
        for tube in range(1, N+2 + 1):
            if  not B[tube]: continue
            peek = B[tube][-1]
            peeks[peek] = peeks.get(peek, set()) | set([tube])
        if  set(len(x) for x in peeks.values()) == set([1]):
            if  set(len(x) for x in B[1:]) == set([0, M]):
                break
            heights = sorted([(i, len(x)) for i, x in enumerate(B[1:], 1)], key=lambda x: (x[1],x[0]), reverse=True)
            toempty = heights[0][0]
            empties = sorted([i for i in range(1, N+2 +1) if not len(B[i])], reverse=True)
            destination = empties[0]
            peek_ = B[toempty][-1]
            P, Q = toempty, destination
            while B[toempty][-1] == peek_:
                if  len(B[Q]) == L[Q]:
                    ops.append((2, Q))
                    cost += C[Q]
                    L[Q] += 1
                ops.append((1, P, Q))
                cost += 0
                B[Q].append(B[P].pop())
        else:
            spreading = sorted(peeks.items(), key=lambda x: (len(x[1]),x[0]), reverse=True)
            topour = spreading[0][1]
            destination = sorted([(x,C[x]) for x in topour], key=lambda x: (x[1],-x[0]))[0][0]
            topour.remove(destination)
            Q = destination
            for P in topour:
                if  len(B[Q]) == L[Q]:
                    ops.append((2, Q))
                    cost += C[Q]
                    L[Q] += 1
                ops.append((1, P, Q))
                cost += 0
                B[Q].append(B[P].pop())
    if debug: disp(N, M, C, D, B, L)
    return ops
N, M = [int(x) for x in input().strip().split()[:2]]
C    = [int(x) for x in input().strip().split()[:N+2]]
D, B = [], []
for _ in range(N):
    Di = [int(x) for x in input().strip().split()[:N]]
    D.append([None]+Di)
for _ in range(N):
    Bi = [int(x) for x in input().strip().split()[:M]]
    B.append(Bi)
B.append([])
B.append([])
L = [M] * (N + 2)
for X in (C, D, B, L): X.insert(0, None)
ops = main(N, M, C, D, B, L)
print(0, len(ops))
for op in ops: print(' '.join(str(x) for x in op))
