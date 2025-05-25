
# best complexity - O(n)
# average complexity - O(n2)
# worst complexity - O(n2)


def insertion_sort(arr):

    for i in range(len(arr)):
        j=i
        while((j > 0) and (arr[j-1]>arr[j])):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    
    return arr


arr=[23,45,1,28,4,23,4,5]
print(insertion_sort(arr))