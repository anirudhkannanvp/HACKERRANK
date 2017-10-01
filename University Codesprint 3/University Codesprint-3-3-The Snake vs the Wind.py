si=int(input())
table = [[0 for x in range(si)] for y in range(si)] 
dire=input()
stx,sty=map(int,input().split())
no=0
table[stx][sty]=no

#(0,0)
if(dire=='n' and stx==0 and sty==0):
    k=1
    for i in range(si):
        if(k==1):
            for j in range(si):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for j in range(si-1,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
elif(dire=='w' and stx==0 and sty==0):
    k=1
    for j in range(si):
        if(k==1):
            for i in range(si):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for i in range(si-1,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
elif(dire=='e' and stx==0 and sty==0):
    for j in range(si):
        no+=1
        table[stx][j]=no
    k=1
    for j in range(si-1,-1,-1):
        if(k==1):
            for i in range(1,si):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for i in range(si-1,0,-1):
                no+=1
                table[i][j]=no
            k*=-1           
elif(dire=='s' and stx==0 and sty==0):
    for i in range(si):
        no+=1
        table[i][sty]=no               
    k=1
    for i in range(si-1,-1,-1):
        if(k==1):
            for j in range(1,si):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for j in range(si-1,0,-1):
                no+=1
                table[i][j]=no
            k*=-1            
                

                
#(si,0)
elif(dire=='s' and stx==si-1 and sty==0):
    k=1
    for i in range(si-1,-1,-1):
        if(k==1):
            for j in range(si):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for j in range(si-1,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
elif(dire=='w' and stx==si-1 and sty==0):
    k=1
    for j in range(si):
        if(k==1):
            for i in range(si-1,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for i in range(si):
                no+=1
                table[i][j]=no
            k*=-1
elif(dire=='n' and stx==si-1 and sty==0):
    for i in range(si-1,-1,-1):
        no+=1
        table[i][sty]=no
    k=1
    for i in range(si):
        if(k==1):
            for j in range(1,si):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for j in range(si-1,0,-1):
                no+=1
                table[i][j]=no
            k*=-1           
elif(dire=='e' and stx==si-1 and sty==0):
    for j in range(si):
        no+=1
        table[stx][j]=no                
    k=1
    for j in range(si-1,-1,-1):
        if(k==1):
            for i in range(si-2,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for i in range(si-1):
                no+=1
                table[i][j]=no
            k*=-1            
                
                
                
                
#(0,si)
elif(dire=='e' and stx==0 and sty==si-1):
    k=1
    for j in range(si-1,-1,-1):
        if(k==1):
            for i in range(si):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for i in range(si-1,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
elif(dire=='n' and stx==0 and sty==si-1):
    k=1
    for i in range(si):
        if(k==1):
            for j in range(si-1,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for j in range(si):
                no+=1
                table[i][j]=no
            k*=-1
elif(dire=='s' and stx==0 and sty==si-1):
    for i in range(si):
        no+=1
        table[i][sty]=no               
    k=1
    for i in range(si-1,-1,-1):
        if(k==1):
            for j in range(si-2,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for j in range(si-1):
                no+=1
                table[i][j]=no
            k*=-1              
elif(dire=='w' and stx==0 and sty==si-1):
    for j in range(si-1,-1,-1):
        no+=1
        table[stx][j]=no
    k=1
    for j in range(si):
        if(k==1):
            for i in range(1,si):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for i in range(si-1,0,-1):
                no+=1
                table[i][j]=no
            k*=-1
                        
#(si,si)
elif(dire=='e' and stx==si-1 and sty==si-1):
    k=1
    for j in range(si-1,-1,-1):
        if(k==1):
            for i in range(si-1,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for i in range(si):
                no+=1
                table[i][j]=no
            k*=-1
elif(dire=='s' and stx==si-1 and sty==si-1):
    k=1
    for i in range(si-1,-1,-1):
        if(k==1):
            for j in range(si-1,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for j in range(si):
                no+=1
                table[i][j]=no
            k*=-1
elif(dire=='w' and stx==si-1 and sty==si-1):
    for j in range(si-1,-1,-1):
        no+=1
        table[stx][j]=no
    k=1
    for j in range(si):
        if(k==1):
            for i in range(si-2,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for i in range(si-1):
                no+=1
                table[i][j]=no
            k*=-1
elif(dire=='n' and stx==si-1 and sty==si-1):
    for i in range(si-1,-1,-1):
        no+=1
        table[i][sty]=no
    k=1
    for i in range(si):
        if(k==1):
            for j in range(si-2,-1,-1):
                no+=1
                table[i][j]=no
            k*=-1
        else:
            for j in range(si-1):
                no+=1
                table[i][j]=no
            k*=-1
for i in range(si):
    for j in range(si):
        print(table[i][j],sep=" ",end=" ")
    print()