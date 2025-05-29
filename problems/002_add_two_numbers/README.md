
# [002] Add Two Numbers

## Problem Description
- **Link**: [https://leetcode.com/problems/add-two-numbers)

### Statement
I am given two non-empty linked lists representing two non-negative integers. The digits are stored in a reverse order, and each will contain a single digit. Add two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Examples
- **Example 1**:
  - **Input**: `ls1 = [2, 4, 3]`, `ls2 = [5, 6, 4]`
  - **Output**: `[7, 0, 8]`
  - **Explanation**: Because 342 + 465 = 807

- **Example 2**:
  - **Input**: `ls1 = [0]`, `ls2 = [0]`
  - **Output**: `[0]`

- **Example 3**:
  - **Input**: `ls1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
  - **Output**: `[8,9,9,9,0,0,0,1]'

### Constraints
- The number of nodes in each linked list is in the range [1, 100]
- 0 <= node.val <= 9
- It is guranteered that the list represents a number that does not have leading zeros

## Additional Resources
- **Solution**: [solution.py](solution.py) – Python code for solving the problem.
- **Notes**: [notes.md](notes.md) – My thought process, analogies, and neurodivergent-friendly explanations.
