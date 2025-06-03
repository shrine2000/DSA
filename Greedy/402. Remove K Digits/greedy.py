class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Removes k digits from a number string to make the new number the smallest possible.

        This function uses a monotonic stack approach. It iterates through the digits
        of the input number and maintains a stack such that the digits in the stack
        are always in non-decreasing order. When a new digit is encountered that is
        smaller than the top of the stack, digits are popped from the stack (removed)
        until the stack's top is less than or equal to the new digit, or k removals
        are exhausted.
        """
        # Initialize an empty list to serve as our monotonic stack.
        # This stack will store digits that form the smallest possible number.
        stack = []

        # Iterate through each digit in the input number string.
        for digit in num:
            # While the stack is not empty, we still have removals left (k > 0),
            # and the last digit added to the stack (stack[-1]) is greater than
            # the current digit being processed (digit).
            # This is the core of the monotonic stack: we remove larger digits
            # from the left if a smaller digit appears on the right, as this
            # leads to a smaller number.
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()  # Remove the larger digit from the stack.
                k -= 1  # Decrement the count of digits to remove.

            # Handle leading zeros:
            # A digit should only be appended to the stack if:
            # 1. The stack is not empty (meaning we've already placed a non-zero digit
            #    or are in the middle of the number).
            # 2. OR, the current digit is not '0'. This prevents adding leading zeros
            #    to an empty stack (e.g., "0123" should become "123").
            if stack or digit != "0":
                stack.append(digit)

        # After iterating through all digits, if we still have 'k' removals left,
        # it means we couldn't remove k digits by the monotonic rule (e.g., the
        # remaining digits are already in increasing order, like "12345").
        # In such cases, we simply remove the last 'k' digits from the stack,
        # as removing digits from the end of an increasing sequence yields the
        # smallest result.
        if k > 0:
            stack = stack[:-k]

        # Join the digits in the stack to form the result string.
        # If the stack becomes empty (e.g., num="10", k=2), the result should be "0".
        # The `or '0'` handles this edge case.
        return "".join(stack) or "0"
