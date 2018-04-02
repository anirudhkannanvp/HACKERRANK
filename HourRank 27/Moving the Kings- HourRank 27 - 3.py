n,k=map(int,input().split())
ki=[]
c=0
for i in range(n):
    a,b=map(int,input().split())
    ki.append([a,b])
for i in range(k):
    c=0
    a,b=map(int,input().split())
    for j in range(n):
        a1=ki[j][0]
        a2=ki[j][1]
        xdist=abs(a-a1)
        ydist=abs(b-a2)
        diagdist=min(xdist,ydist)
        xdist-=diagdist
        ydist-=diagdist
        c+=diagdist+xdist+ydist
    print(c)