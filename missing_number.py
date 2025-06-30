def missing_n(arr):
    
    s=(len(arr)*(len(arr)+1)) / 2
    
    rem=0
    for i in arr:
        rem+=i
        
    return (s-rem)

print(missing_n([1,3,0,5]))


# BRUTE FORCE

# def miss(arr):
#     d={}

#     for i in range(0,len(arr)):
#         if arr[i] in d:
#             d[arr[i]]+=1

#         else:
#             d.update({arr[i] : 1})

    
#     for k,v in d.items():
#         if v==1:
#             return(k)
        

# print(miss([12,12,2,2,3]))