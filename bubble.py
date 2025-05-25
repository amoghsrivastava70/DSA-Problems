
# best complexity - O(n)
# average complexity - O(n2)
# worst complexity - O(n2)

def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        temp=False
        for j in range(0,i):
            
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print("Running..")
                temp=True
        
        if(temp == False):
            print("Sorted")
            break

    return arr


arr=[214,25,457,55,2,1,789,586]
arr2=[1,2,3,4,5]

            

print(bubble_sort([2,45,1]))