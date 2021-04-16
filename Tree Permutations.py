from collections import defaultdict as dd
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(cur, prev):
    global par, childs
    par[cur] = prev
    childs[cur] = len(tree[cur]) - 1
    for i in tree[cur]:
        if i != prev:
            dfs(i, cur)
def dfs2(cur, prev):
    global childs
    childs[cur] = len(tree[cur]) - 1
    for i in tree[cur]:
        if i != prev:
            dfs2(i, cur)
mod = 10**9 + 7
for _ in range(int(input())):
    n, s = map(int, input().split())
    tree = dd(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
    tree[-1].append(0)
    tree[0].append(-1)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n == 1:
        if a[0] == b[0]:
            print(1)
        else:
            print(0)
        continue
    leafs = []
    for i in range(1, n):
        if len(tree[i]) == 1:
            leafs.append(i)
    par = [ i for i in range(n) ]
    childs = [ 0 for i in range(n) ]
    dfs(0, -1)
    vis = [ 0 for i in range(n) ]
    ans = 1
    vertical_partition = []
    while(leafs):
        cnt = {}
        cur = leafs.pop(0)
        f = 1
        while(cur != -1):
            if vis[cur]:
                ans = 0
                break
            cnt[ a[cur] ] = cnt.get( a[cur], 0) + 1
            cnt[ b[cur] ] = cnt.get( b[cur], 0) - 1
            vis[cur] = 1
            if f:
                vertical_partition.append(cur)
                f = 0
            if cnt.get(a[cur], None) != None and cnt[ a[cur] ] == 0:
                cnt.pop(a[cur])
            if cnt.get(b[cur], None) != None and cnt[ b[cur] ] == 0:
                cnt.pop(b[cur])
            if len(cnt) == 0:
                if par[cur] == -1:
                    break
                childs[par[cur]] -= 1
                if childs[par[cur]] == 0 and not vis[par[cur]]:
                    leafs.append(par[cur])
                break
            cur = par[cur]
        if len(cnt) != 0:
            ans = 0
        if ans == 0:
            break
    if s == 1:
        print(ans)
        continue
    v = len(vertical_partition)
    childs = [ 0 for i in range(n) ]
    dfs2(0, -1)
    for i in range(v):
        ans = ans*(childs[vertical_partition[i]] + 1)
        ans %= mod
    print(ans%mod)
