def sec_lar(num):
    max_1=0
    for i in num:
        if i > max_1:
            max_1=i

    max_2=0
    for j in num:
        if (j != max_1 and j >max_2 ):
            max_2=j

    return (f"largest 1: {max_1} , largest 2: {max_2}") 


ans=sec_lar([12,3,4,78,88])
print(ans)