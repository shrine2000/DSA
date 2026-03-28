```python
function slidingWindow(data):
    left = 0
    # Initialize data structure to track window state (e.g., a hash map, sum variable)
    window_state = ...
    # Initialize result variable
    result = ...

    for right in range(len(data)):
        # 1. Expand the window by including the element at the 'right' pointer
        add_element_to_window_state(window_state, data[right])

        # 2. Process the window and update the result if necessary
        # This step often involves checking if the current window satisfies the problem's condition
        update_result(result, window_state, left, right)

        # 3. Shrink the window from the left if a certain condition is met
        # This condition is problem-specific and often involves maintaining a constraint
        while window_needs_to_shrink(window_state, left, right):
            remove_element_from_window_state(window_state, data[left])
            left += 1
            # Optionally, update the result again after shrinking if needed
            # update_result(result, window_state, left, right)

    return result
```

### 1. Fixed Size Window
```python
def fixed_window(arr, k):
    # initialize window state
    window_state = 0
    result = 0

    for r in range(len(arr)):
        # add arr[r] to window
        window_state += arr[r]

        # remove leftmost element once window exceeds size k
        if r >= k:
            window_state -= arr[r - k]

        # update result (only when window is fully formed)
        if r >= k - 1:
            result = max(result, window_state)

    return result
```

### 2. Variable Size Window
```python
def variable_window(arr, k):
    # initialize window state
    window_state = 0
    result = 0
    l = 0

    for r in range(len(arr)):
        # add arr[r] to window
        window_state += arr[r]

        # shrink window from left until valid
        while not valid(window_state, k):
            window_state -= arr[l]
            l += 1

        # update result (window is always valid here)
        result = max(result, r - l + 1)

    return result
```