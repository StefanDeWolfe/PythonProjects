# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


# Author: Stefan DeWolfe
# Created April 2022
def sumOfTwoIndexes(numberArray, target):
    for i in range(len(numberArray)):
        candidate = target - numberArray[i]
        if (candidate in numberArray and numberArray.index(candidate) != i):
            return sorted([numberArray.index(candidate), i])
    
    return None

print(sumOfTwoIndexes([2,7,11,15], 9))
print(sumOfTwoIndexes([3,2,4], 6))
print(sumOfTwoIndexes([3,3], 6))