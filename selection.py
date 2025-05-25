
# best complexity - O(n2)
# average complexity - O(n2)
# worst complexity - O(n2)

def selection_sort(arr):

    for i in range(0 , (len(arr)-1)):
        
        min=i
        for j in range(i+1 , (len(arr))):
            if arr[j]<arr[min]:
                arr[j],arr[min]=arr[min],arr[j]
    
    return arr

arr=[12,1,34,2,45,3,1]
print(selection_sort(arr))

        