def rem(arr):
    
    i=0
    for j in range(1 , len(arr)):
        if (arr[i] != arr[j]):
            arr[i+1]=arr[j]
            i+=1
    return (arr , i+1)


arr , unique = rem([1,1,2,2,3,3,4,4,5])
print(arr , unique)