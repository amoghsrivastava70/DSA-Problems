

def merge(arr,st,mid,end):

    temp=[]
    i=st
    j=mid+1

    while (i<=mid and j<=end):
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    
    while(i<=mid):
        temp.append(arr[i])
        i+=1

    while(j<=end):
        temp.append(arr[j])
        j+=1

    for i in range(len(temp)-1):
        arr[i+st]=temp[i]


def mergeSort(arr , st ,end):

    if (st<end):
        mid=st+((end-st)//2)

        mergeSort(arr,st,mid)  #left
        mergeSort(arr,mid+1,end)   #right

        merge(arr,st,mid,end)


arr=[20,1,45,7,89,9]
mergeSort(arr,0,len(arr)-1)
print(arr)