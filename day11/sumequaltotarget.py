l=[7,5,6,4]
left=0
right=len(l)-1
target=20
while left<right:
    if l[left]+l[right]==target:
        print(left,right)
        break
    elif l[left]+l[right]<target:
        left+=1
    else:
        right+=1
