def moves_zero(arr):
    k=-1
    
    for i in range(0,len(arr)):
        if arr[i]==0:
            k=i
            break
    if k == -1:
        return arr
    for i in range(k+1 ,len(arr)):
        if arr[i] != 0:
            arr[i],arr[k]=arr[k],arr[i]
            k+=1
            
            
    return arr


# ans=moves_zero([1,2,00,0,5,6,0,0,12])
ans=moves_zero([12,45,48])
print(ans)
            