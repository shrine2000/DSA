def find_next_greater_elements(nums):
    # Initialize a list to store the next greater element of every element
    next_greater = [-1] * len(nums)
    
    # Create a stack to keep track of the indices of elements from the input list
    stack = []
    
    # Loop through the circular array
    for i in range(2 * len(nums) - 1):
        # Get the current element from the circular array
        current_element = nums[i % len(nums)]
        
        # Process elements in the stack to find the next greater element
        while stack and nums[stack[-1]] < current_element:
            index = stack.pop()
            next_greater[index] = current_element
        
        # Push the current index onto the stack for further processing
        stack.append(i % len(nums))
    
    return next_greater
