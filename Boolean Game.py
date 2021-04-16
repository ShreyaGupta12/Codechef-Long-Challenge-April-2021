for test in range(int(input())):
    n,m,k1=map(int,input().split())
    g=[0]
    gt=list(map(int,input().split()))
    g.extend(gt)
    pos=[[] for x in range(n+1)]
    for i in range(m):
        u,v,d=map(int,input().split())
        pos[u].append([i,d])
        pos[v].append([i,d])
    dp=[[] for x in range(n+1)]
    dp[0].append([0,0])
    for i in range(1,n+1):
        temp=[]
        temp.extend(dp[i-1])
        cur=0
        mask=0
        open1={}
        for j in range(i,0,-1):
            cur+=g[j]
            mask= mask^ (1<<j)
            for k in pos[j]:
                if(k[0] in open1): cur+=k[1]
                else: open1[k[0]]=1
            if(j>1):
                for k in dp[j-2]: temp.append([k[0]+cur,mask^k[1]])
            else: temp.append([cur,mask])
        temp.sort()
        temp=temp[::-1]
        sel={}
        filled=0
        j=0
        while(j<len(temp) and filled<k1):
            if(temp[j][1] in sel): j+=1
            else:
                dp[i].append(temp[j])
                filled+=1
                sel[temp[j][1]]=1
                j+=1
    dp[n].sort(reverse=True)
    for i in range(k1):
        print(dp[n][i][0],end=" ")
    print()
