# Python3 program for the above approach

# Function to get the missing element
def missingElement(arr, n):
        
        # For maximum element in the array
        max_ele = arr[0]

        # For minimum Element in the array
        min_ele = arr[0]

        # For xor of all elements
        x = 0

        # Common difference of AP series
        d = 0

        # Find maximum and minimum element
        for i in range(n):
            if (arr[i] > max_ele):
                max_ele = arr[i]

            if (arr[i] < min_ele):
                min_ele = arr[i]

        # Calculating common difference
        d = (max_ele - min_ele) // n
        
        # Calculate the XOR of all elements
        for i in range(n):
            x = x + arr[i]
        

        # Perform XOR with actual AP series
        # resultant x will be the ans
        for i in range(n + 1):
            x = x - (min_ele + (i * d))

        # Return the missing element
        return x*-1

# Driver Code
if __name__ == '__main__':
	
        # Given array
        arr = [ 12, 3, 9, 15, 18 ]
        n = len(arr)

        # Function Call
        element = missingElement(arr, n)

        # Print the missing element
        print(element)

