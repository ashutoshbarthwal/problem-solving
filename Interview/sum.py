# unsorted array
# kth largest element

# [2,89,23,1,8,19,40]
# k = 3
# [23,40,89]

# array a and b
# contains large number
a = [9,9,9]
b = [9,9,9]

def sumArray(a,b):
    n = len(a)
    m = len(b)
    k = n
    if m > n:
        k = m
    sum = []
    add = 0
    for i in range(1,k+1):
        if i <=n:
            A = a[-i]
        else:
            A = 0
        if  i<=m:
            B = b[-i]
        else:
            B = 0
        temp = A+B+add
        if temp > 9:
            add = 1
            temp = temp%10
        else:
            add = 0
        sum.append(temp)
    if add == 1:
        sum.append(1)
    
    return sum[::-1]

print(sumArray(a,b))
# Block
# {
#     val : 1
#     next : Block(2)
#     ladder : Block(6)
#     snake: None
# }
# {
#     1:6,
#     99:2
# }

# current = Block(6)
# #
# Player
# Block
# Ladder [Block -> Block]
# Snake [Block -> Block]
# Move



