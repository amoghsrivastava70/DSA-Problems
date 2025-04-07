def missing_n(arr):
    
    s=(len(arr)*(len(arr)+1)) / 2
    
    rem=0
    for i in arr:
        rem+=i
        
    return (s-rem)

print(missing_n([1,3,0,5]))