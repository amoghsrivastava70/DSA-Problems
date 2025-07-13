# With Space O(n) and time O(n)
# def rotate_arr(arr , d):

#     d=(d)%len(arr)
#     lst2=[0]*len(arr)

#     for j in range(0,len(arr)):
#         lst2[(j+d)%len(arr)]=arr[j]


#     return lst2



# print(rotate_arr([1,2,3,4,5,6,7] ,2))



def rotate_arr(arr , d):

    d=(d)%len(arr)

    def rev(ar ,l,r):
        
        while l<r:
            ar[l],ar[r]=ar[r],ar[l]
            l+=1
            r-=1
        

    rev(arr,0,len(arr)-1)
    rev(arr,0,d-1)
    rev(arr,d,len(arr)-1)
    
    return arr

print(rotate_arr([1,2,3,4,5,6,6],3))


