def sec_max(arr):
    max=arr[0]
    sec=-1
        
    for i in arr:
        if i>max:
            max=i
        
    for j in arr:
        if (j>sec) and (j!=max):
            sec=j
        
    if sec==-1:
        return -1
    else:
        return sec
    

ans=sec_max([10,45,-78,46])
print(ans)