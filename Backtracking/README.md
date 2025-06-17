## Backtracking

* We use dp to solve optimization problems, backtracking is used when there are multiple solutions and all solutions are required.
* backtracking follows DFS




1. [Backtracking Python problems + solutions - interview prep](https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/780232/Backtracking-Python-problems%2B-solutions-interview-prep)
2. [Introduction to Backtracking - Brute Force Approach](https://www.youtube.com/watch?v=DKCbsiDBN6c)
3. [Backtracking - Neetcode](https://www.youtube.com/playlist?list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo)
4. [Backtracking - Aditya Verma](https://www.youtube.com/playlist?list=PL_z_8CaSLPWdbOTog8Jxk9XOjzUs3egMP)
5. [Backtracking PDF](https://jeffe.cs.illinois.edu/teaching/algorithms/book/02-backtracking.pdf)


### Template

```python

def backtrack(choices: List[Any], current_path: List[Any], result: List[List[Any]]):
    if is_solution(current_path):
        result.append(current_path[:])
        return

    for choice in choices:
        if is_valid(choice, current_path):
            current_path.append(choice)
            backtrack(choices, current_path, result)
            current_path.pop()  # backtrack

```