t=int(input())
while(t):
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    c=[]
    for i in range(1,n+1):
        b.append(i)
        c.append(a[i-1])
    c.sort()
    if(a!=b and c==b):
        print("Beautiful")
    else:
        print("Ugly")