def answer():
    xl,yl,xr,yr=-(10**18)-1,-(10**18)-1,(10**18)+1,(10**18)+1
    while(1):
        m1=(xl+xr)//2
        m2=(yl+yr)//2
        print(1,m1,m2)
        s=input()
        if(s=='FAILED'):exit(0)
        if(s=='O'):return
        if(s[0]=='P'):
            xr=m1-(d==0)
            xl-=d
        elif(s[0]=='N'):
            xl=m1+(d==0)
            xr+=d
        else:
            xl=m1-1
            xr=m1+1
        if(s[1]=='P'):
            yr=m2-(d==0)
            yl-=d
        elif(s[1]=='N'):
            yl=m2+(d==0)
            yr+=d
        else:
            yl=m2-1
            yr=m2+1
        if(xr-xl == 2 and yr-yl == 2):
            print(2,xl,yl,xr,yr)
            s=input()
            if(s=='O'):return
            if(s=='FAILED'):exit(0)
        if(xr-xl == 3 and yr-yl == 3):
            print(2,xl,yl,xl+2,yr)
            s=input()
            if(s=='O'):return
            if(s=='FAILED'):exit(0)
            if(s=='IN'):xr=xl+2
            else:
                xr+=1
                xl+=2
        if(xr-xl == 3 and yr-yl == 2):
            print(2,xl,yl,xl+2,yr)
            s=input()
            if(s=='O'):return
            if(s=='FAILED'):exit(0)
            if(s=='IN'):print(2,xl,yl,xl+2,yr)
            else:print(2,xl+2,yl,xl+4,yr)
            s=input()
            if(s=='O'):return
            if(s=='FAILED'):exit(0)
        if(xr-xl == 2 and yr-yl == 3):
            print(2,xl,yl,xr,yl+2)
            s=input()
            if(s=='O'):return
            if(s=='FAILED'):exit(0)
            if(s=='IN'):print(2,xl,yl,xr,yl+2)
            else:print(2,xl,yl+2,xr,yl+4)
            s=input()
            if(s=='O'):return
            if(s=='FAILED'):exit(0)
t,q,d=map(int,input().split())
for T in range(t): answer()
