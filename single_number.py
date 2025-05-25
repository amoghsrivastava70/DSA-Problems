def single_num(arr):
    
    for i in arr:
        ct=0
        for j in arr:
            if i==j:
                ct+=1
            print(ct)  
            
        
    
single_num([1,1,2,2,0])
            