

def two_sum(arr , target):
    prev={}
    for index , i in enumerate(arr):
        remain=target-i
        if (remain in prev):
            return(f"Indexes are : [{prev[remain]},{index}]")
        
        else:
            prev.update({i : index})
    
    return "Not Found"

arr=[20,45,3,23,12,10,23]
ans=two_sum(arr,33)
print(ans)


