def find_previous_greater_index(arr):
    stack = []
    
    previous_greater = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        
        if stack:
            previous_greater[i] = arr[stack[-1]]
        
        stack.append(i)
        
    return previous_greater

arr = [10, 4, 2, 20, 40, 12, 30]
expected = [-1, 10, 4, -1, -1, 40, 40]
result = find_previous_greater_index(arr)
print(result == expected) 