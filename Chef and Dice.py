for _ in range(int(input())):
    n=int(input())
    x=n%4
    y=n//4
    a2=0
    b3=0
    c4=0
    d5=0
    e=0
    f=0
    if x==1: d5=1
    elif x==2: c4=2
    elif x==3: 
        c4=2
        b3=1
    if y>0 :
        a2+=y*4
        f=(4-x)*4
    print((a2*11)+(b3*15)+(c4*18)+(d5*20)+f)
