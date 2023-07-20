def  find_next_greater_index(arr):
    stack = []
    next_greater = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            stack_top = stack.pop()
            next_greater[stack_top] = i
        stack.append(i)
        
    return next_greater

#       0  1  2  3   4 
arr1 = [4, 5, 2, 25, 10]
expected1 = [1, 3, 3, -1, -1]
result1 = find_next_greater_index(arr1)
print(result1 == expected1)