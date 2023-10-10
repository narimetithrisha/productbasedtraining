#floor means if se=89 then it should return the least near value means 59  
def binarysearch(l,si,li,se):
    mid=(si+li)//2
    if si>li:
        return l[mid]
    if se<l[0]:
        return -1
    if l[mid]==se:
        return True
    if l[mid]<se:
        return binarysearch(l,mid+1,li,se)
    return binarysearch(l,si,mid-1,se)
    
l=[24,37,49,59,90]
print(binarysearch(l,0,len(l)-1,23))
