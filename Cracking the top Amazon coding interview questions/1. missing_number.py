# 1. Find the missing number in the array
# You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. The input array is not sorted. Look at the below array and give it a try before checking the solution.

# 3
# 7
# 1
# 2
# 8
# 4
# 5
# n = 8 missing number = 6

# Runtime Complexity: Linear, O(n)
# O(n)

# Memory Complexity: Constant, O(1)
# O(1)


def find_missing(input):
    sum = 0
    for i in input:
        sum += i
    n = len(input) + 1
    return n * (n + 1) / 2 - sum


print(find_missing([3, 7, 1, 2, 8, 4, 5,6 ]))