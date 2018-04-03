for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if(n==1):
        print("YES")
        continue
    for i in range(n):
        b=a[:]
        if(i>0):
            b[i]=b[i-1]
            if(b==sorted(b)):
                print("YES")
                break
        b=a[:]
        if(i<n-1):
            b[i]=b[i+1]
            if(b==sorted(b)):
                print("YES")
                break
    else:
        print("NO")