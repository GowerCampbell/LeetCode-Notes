# [001] Two Sum

## Problem Description
- **Link**: [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

### Statement
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to the `target`. You may assume that each input has **exactly one solution**, and you may not use the same element twice. The answer can be returned in any order.

### Examples
- **Example 1**:
  - **Input**: `nums = [2, 7, 11, 15]`, `target = 9`
  - **Output**: `[0, 1]`
  - **Explanation**: Because `nums[0] + nums[1] = 2 + 7 = 9`, return `[0, 1]`.

- **Example 2**:
  - **Input**: `nums = [3, 2, 4]`, `target = 6`
  - **Output**: `[1, 2]`
  - **Explanation**: Because `nums[1] + nums[2] = 2 + 4 = 6`, return `[1, 2]`.

- **Example 3**:
  - **Input**: `nums = [3, 3]`, `target = 6`
  - **Output**: `[0, 1]`
  - **Explanation**: Because `nums[0] + nums[1] = 3 + 3 = 6`, return `[0, 1]`.

### Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Exactly one valid solution exists.**

### Follow-Up
Can you come up with an algorithm that has a time complexity less than `O(n^2)`?

## Additional Resources
- **Solution**: [solution.py](solution.py) – Python code for solving the problem.
- **Notes**: [notes.md](notes.md) – My thought process, analogies, and neurodivergent-friendly explanations.
- **Visual**: [visual.png](visual.png) – Diagram illustrating the problem (if available).
