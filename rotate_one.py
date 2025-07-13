
def rotate_one(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=temp


    return arr


print(rotate_one([2,3,4,5,6]))
