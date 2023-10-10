nums=[5,8,1,2,3]
nums.sort()
print(nums)
target=5

flag=False
for i in range(len(nums)-2):
    j=i+1
    k=len(nums)-1
    while j<k:
        if nums[i]+nums[j]+nums[k]==target:
            flag=True
            print(nums[i],nums[j],nums[k])
        elif nums[i]+nums[j]+nums[k]<target:
            j+=1
        elif nums[i]+nums[j]+nums[k]>target:
            k-=1
if flag:
    print("found")
else:
    print("Not found")
