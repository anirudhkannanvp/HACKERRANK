for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if(sum(a)%3==0):
        print("Yes")
    else:
        print("No")