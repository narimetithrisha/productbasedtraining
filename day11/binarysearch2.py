def binary_search(arr,low,high,key):
  if high>=low:
    mid=(low+high)//2
    if arr[mid]==key:
        return mid
    if key<arr[mid]:
      return binary_search(arr,low,mid-1,key)
    if key>arr[mid]:
      return binary_search(arr,mid+1,high,key)
    


arr=[1,2,3,4,5,6,7,8,9]
key=7
res=binary_search(arr,0,len(arr)-1,key)
print("element is pre at:",res)

