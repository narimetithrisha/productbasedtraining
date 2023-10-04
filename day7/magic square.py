'''1)for 1st number(n//2,n-1)
2)next number->(i-1,j+1)
3)if box if filled/already number exist then use i=i+1 and j=j-2
4)if  the number goes out of the box then i=0 and j=n-2'''

n=int(input())
sq=[[0]*n for i in range(n)]
num=1
i=n//2
j=n-1
while num<=(n*n):
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
    if sq[i][j]:
        i=i+1
        j=j-2
        continue
    sq[i][j]=num
    num+=1
    i=i-1
    j=j+1
print(sq)
    
