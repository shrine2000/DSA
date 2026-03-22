# Agent Guide (agents.md)

Welcome, agent. This repository is a collection of Data Structures and Algorithms (DSA) problems, primarily from LeetCode and GeeksforGeeks.

## Repository Structure

### 1. Numbered Problem Folders
Each problem is contained in a folder named `XXXX-problem-name/` at the root.
- `README.md`: Contains the problem statement, usually in HTML format.
- `XXXX-problem-name.py`: The Python solution(s). Multiple approaches (e.g., Brute Force, Optimal) should be included in the same file or clearly separated.
- `NOTES.md`: Optional file for personal notes or complexity analysis.

### 2. Topic-Specific Folders
Problems are also categorized into topic-specific folders such as `Trie/`, `Dynamic Programming/`, `Graphs/`, etc.
- If a problem fits a specific structure (like a Trie), create a subfolder within the topic folder: `Topic/problem-name/`.
- Inside the subfolder, separate approaches into different files: `brute-force.py`, `optimised.py`.

## Workflow for Adding New Problems
1. Create the numbered problem folder at the root.
2. Add the `README.md` with the problem statement.
3. Add the solution file with clear comments on the approach and complexity.
4. Identify the relevant topic folder and add the solution there as well (following the topic-specific structure).
5. Update the root `README.md` if necessary (though it currently only links to topic folders).

## Principles
- Use clear, descriptive comments.
- Include Time and Space Complexity for all solutions.
- If multiple approaches exist, label them clearly (e.g., Approach 1, Approach 2).
- Follow PEP 8 style for Python code.
