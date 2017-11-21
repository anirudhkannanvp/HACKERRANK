n,m,k=map(int,input().split())
a=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if(i==0 and j==0):
            a[i][j]=m
        elif(i==j):
            a[i][j]=a[i-1][j-1]+k
        elif(i>j):
            a[i][j]=a[i-1][j]-1
        else:
            a[i][j]=a[i][j-1]-1
for i in range(n):
    for j in range(n):
        print(a[i][j],sep=" ",end=" ")
    print()