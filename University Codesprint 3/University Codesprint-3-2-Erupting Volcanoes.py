si=int(input())
table = [[0 for x in range(si)] for y in range(si)] 
t=int(input())
t1=t
ans=-1
while(t):
    t=t-1
    m,n,p=map(int,input().split())
    table[m][n]+=p
    temp=int(p)
    startx=m
    endx=m
    endy=n
    starty=n
    while(temp>0):
        startx-=1
        endx+=1
        starty-=1
        endy+=1
        temp-=1
        for i in range(starty,endy+1):
            if(startx>=0 and i>=0 and i<=si-1 and startx<=si-1):
                table[startx][i]+=temp
        for i in range(startx+1,endx):
                if(starty>=0 and i>=0 and i<=si-1 and starty<=si-1):
                    table[i][starty]+=temp
        for i in range(startx+1,endx):
                if(endy>=0 and endy<=si-1 and i<=si-1 and i>=0):
                    table[i][endy]+=temp
        for i in range(starty,endy+1):
                if(endx>=0 and endx<=si-1 and i<=si-1 and i>=0):
                    table[endx][i]+=temp
ans=-1
for i in range(si):
    for j in range(si):
        ans=max(ans,table[i][j])
print(ans)