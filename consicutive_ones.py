def consicutive_ones(arr):
    
    max=0
    cons=0
    
    for i in range(0 , len(arr)):
        if arr[i]==1:
            cons+=1
            if cons>max:
                max=cons
                
        elif arr[i]==0:
            cons=0
    
    return max


print(consicutive_ones([1,1,0,1,1,1,1,0]))