# Iterative Binary Search Function method Python Implementation 
# It returns index of n in given list1 if present,  
# else 
 
        # If n is smaller, compared to the left of mid 
        else: 
            return mid 
 
            # element was not present in the list, return -1 
    return -1 
 
 
# Initial list1 
list1 = [12, 24, 32, 39, 45, 50, 54] 
n = 45 
 
# Function call  
result = binary_search(list1, n) 
 
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in list1")