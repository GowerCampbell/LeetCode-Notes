# Assumption: 
# Taking from a list of integers to numbers that will then add together to form the targeted value.

"""
Test:
Indexes the list by counting the total value of list items using the len function: 
if i in range(len(nums)) 

Creates a sequence of numbers starting from the first number in the list through n to the amount in the list counted by my i: 
for n in range(i + 1, len(nums));

Using the + operation to find what equals
if nums[n] + nums[i] == target;

Then return [i, n]
"""

class Solution:
    def twoSum(self, nums, target)
        for i in range(len(nums)):
            for n in range(i + 1, len(nums)):
                if nums[n] + nums[i] == target:
                    return [i, n]
        
