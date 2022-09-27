# 2. Determine if the sum of two integers is equal to the given value
# Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists and return false if it does not. Consider this array and the target sums:

# 5
# 7
# 1
# 2
# 8
# 4
# 3
# Target Sum
# 10
# 7+3=10, 2+8=10
# Target Sum
# 19
# No 2 values sum up to 19



# Runtime Complexity: Linear, O(n^2)

# Memory Complexity: Linear, O(1)
import cProfile
def find_sum_of_two(A, val):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == val:
                return True
    return False

# Runtime Complexity: Linear, O(n)

# Memory Complexity: Linear, O(n)
def find_sum_of_two_better(A, val):
    found_values = set()
    for i in A:
        if val - i in found_values:
            return True
        found_values.add(i)
    return False
array_size = 10000
multuplier = 1
sum =12900
array_size *= multuplier
sum *= multuplier
test_array = range(1, array_size)
find_sum_of_two(test_array, sum)
cProfile.run('find_sum_of_two_better(test_array, sum)')
cProfile.run('find_sum_of_two(test_array, sum)')

# print(find_sum_of_two([5,7,1,2,8,4,3], 19))