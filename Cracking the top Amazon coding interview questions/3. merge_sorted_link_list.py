# 3. Merge two sorted linked lists
# Given two sorted linked lists, merge them so that the resulting linked list is also sorted. Consider two sorted linked lists and the merged list below them as an example.

# head1
# 4
# 8
# 15
# 19
# NULL
# head2
# 7
# 9
# 10
# 16
# NULL
# head1
# 4
# 7
# 8
# 9
# 10
# 15
# 16
# 19
# NULL

# Runtime Complexity: Linear, O(m + n)
# O(m+n)
#  where m and n are lengths of both linked lists

# Memory Complexity: Constant, O(1)
# O(1)

def merge_sorted(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    
    mergeHead = None

    if head1.data < head2.data:
        mergeHead = head1
        mergeHead.next = merge_sorted(head1.next, head2)
    else:
        mergeHead = head2
        mergeHead.next = merge_sorted(head1, head2.next)
    
    return mergeHead


# Python3 implementation of the approach 
import math
  
# Representation of a node
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
# Function to insert node
def insert(root, item):
    temp = Node(item)
      
    if (root == None):
        root = temp
    else :
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
      
    return root
  
def display(root):
    while (root != None) :
        print(root.data, end = " ")
        root = root.next
          
def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])
      
    return root


array1 = [2, 3, 5, 6,19,178,362,589]
array2 = [1, 4, 10,133,299,310,982,1234,1235]
list_head1 = arrayToList(array1,len(array1))
print("Original1:")
display (list_head1)
list_head2 = arrayToList(array2,len(array2))
print("\nOriginal2:")
display (list_head2)
new_head = merge_sorted(list_head1, list_head2)

print("\nMerged:")
display(new_head)