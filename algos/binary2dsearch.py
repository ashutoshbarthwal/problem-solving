# import List
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])
        
    
    # def findTargetin1D(arr: List[int],l:int,target:int):
    #     if arr[l]==target:
    #         return True
    #     elif arr[l] < target:
    #         return findTargetin1D(arr,l//2,target)
    #     else:
    #         return findTargetin1D(arr,l+(l//2),target)
    #     return False
    
    # def findTargetin2D(matrix: List[List[int]],row:int,target:int):
    #     result = False
    #     if(target==matrix[row][0] or target==matrix[row][-1]):
    #         return True
    #     elif (target>=matrix[row][0] or target<=matrix[row][-1]):
    #         return findTargetin1D(matrix[row],len(matrix[row])//2,target)
        
# s = Solution()

import re


def binary_search(arr,l,r,target):
    if r>=l:
        mid = l + (r-l)//2
        # print(mid)
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            return binary_search(arr,l,mid-1,target)
        else:
            return binary_search(arr,mid+1,r,target)
    return False

def binary_search_2d(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    # print(m,n)
    if m==0 or n==0:
        return False
    l = 0
    r = n
    row = find_row(matrix,0,m,target)
    if row == -1:
        return False
    return binary_search(matrix[row],l,r,target)

def find_row(matrix,l,r,target):
    
    if r>=0:
        mid = l + (r-l)//2
        # print("l r",l,r)
        # print("mid",mid)
        if l > r:
            return l
        elif matrix[mid][0] <= target and matrix[mid][-1] >= target:
            return mid
        elif matrix[mid][0] > target:
            # print("matrix[mid][0] > target:",matrix,l,mid-1,target)
            return find_row(matrix,l,mid-1,target)
        elif matrix[mid][-1] < target:
            # print("matrix[mid][0] < target:",matrix,l,mid+1,target)
            return find_row(matrix,mid+1,r,target)
        else:
            return -1
    return -1
    
    

print(binary_search_2d([[1, 3, 5, 7], [21, 22, 23, 25], [28, 30, 34, 60]],2))
print(binary_search_2d([[1, 3, 5, 7], [10, 11, 16, 20], [21, 22, 23, 25], [28, 30, 34, 60]],26))
print(binary_search_2d([[1, 3, 5, 7], [10, 11, 16, 20], [21, 22, 23, 25], [28, 30, 34, 60]],28))
            