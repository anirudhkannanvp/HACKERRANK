n=int(input())
a=list(input())
ans=0
st1=0
st2=0
st3=0
st4=0
for i in range(n):
    if(a[i]=='0' or a[i]=='1' or a[i]=='1' or a[i]=='2' or a[i]=='3' or a[i]=='4' or a[i]=='5' or a[i]=='6' or a[i]=='7' or a[i]=='9' or a[i]=='8'):
        if(st1==0):
            st1=1
            ans+=1
    if(ord(a[i])>=65 and ord(a[i])<=90):
        if(st2==0):
            st2=1
            ans+=1
    if(ord(a[i])>=97 and ord(a[i])<=122): 
        if(st3==0):
            st3=1
            ans+=1
    if(a[i]=='!' or a[i]=='@' or a[i]=='#' or a[i]=='$' or a[i]=='%' or a[i]=='^' or a[i]=='&' or a[i]=='*' or a[i]=='(' or a[i]==')' or a[i]=='-' or a[i]=='+'):
        if(st4==0):
            st4=1
            ans+=1
if(n>=6):
    print(4-ans)
else:
    if(n+4-ans>=6):
        print(4-ans)
    else:
        print(max(6-n,4-ans))
#print(st1,st2,st3,st4)