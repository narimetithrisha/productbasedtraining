def sum(l,low,high):
    if low==high:
      return l[low]
    if low>high:
     return -1
    mid =(low+high)//2
    left=sum(l,low,mid)
    right=sum(l,mid+1,high)
    return left+right

l=[1,2,3,4,5,9,8]
search=10
s=sum(l,0,len(l)-1)
print(s)
