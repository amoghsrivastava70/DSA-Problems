# The XOR operation returns false if any of operands are same ( f ,f = f or t ,t = f)



def single_num(arr):
    xor=0
    for i in arr:
        xor^=i

    return xor


print(single_num([1,1,2,2,3,4,4]))