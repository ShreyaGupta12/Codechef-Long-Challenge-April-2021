from numpy import prod
for _ in range(int(input())):
    print("YES" if round((100/(prod(list(map(float,input().split()))))),2)<9.58 else "NO")
