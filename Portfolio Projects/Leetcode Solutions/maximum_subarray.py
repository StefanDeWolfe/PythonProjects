# Author: Stefan DeWolfe
# Date: 6/2024
#
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Follow up: If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.
import os
import sys
import typing
from typing import List


class Solution:
    def max_sub_array_nn(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        highest_total = nums[0]
        # N^2 solution
        iterations = 0
        for lowest_index in range(len(nums)):
            for highest_index in range(lowest_index, len(nums)):  # remember to start at the LOWER index
                iterations += 1
                sub_sum = sum(nums[lowest_index:highest_index+1])  # REMEMBER the end is non-inclusive
                if sub_sum >= highest_total:
                    highest_total = sub_sum
        print(f"***Iterations: {iterations}")
        return highest_total

    def max_sub_array_nn2(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        highest_total = nums[0]
        # O(N) solution, start at an index, then add the ones following after it, check against highest.
        iterations = 0
        for lowest_index in range(len(nums)):
            total = nums[lowest_index]
            if lowest_index+1 < len(nums):
                for highest_index in range(lowest_index+1, len(nums)):  # remember to start at the LOWER index
                    iterations += 1
                    total += nums[highest_index]
                    if total >= highest_total:
                        highest_total = total
        print(f"***Iterations: {iterations}")
        return highest_total

    # Dresden's solution.
    def max_sub_array_n(self, nums: List[int]) -> int:
        # TIME -> O(n)
        # SPACE -> O(1)
        maxSum = nums[0]
        currSum = 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum

    def max_sub_array_dnc(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        highest_total = sum(nums)
        # Divide and Conquer Solution.... How? For discussion
        return highest_total

# recursive
# Approach 1 - divide and conquer in O(nlgn)
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        def divideAndConquer(i, j):
            if i == j:
                return nums[i]

            k = (i + j) // 2
            res1 = divideAndConquer(i, k)
            res2 = divideAndConquer(k + 1, j)

            left = leftMax = nums[k]
            for a in range(k - 1, i - 1, -1):
                left += nums[a]
                leftMax = max(left, leftMax)

            right = rightMax = nums[k + 1]
            for a in range(k + 2, j + 1):
                right += nums[a]
                rightMax = max(right, rightMax)

            res3 = leftMax + rightMax
            return max(res1, res2, res3)
        return divideAndConquer(0, len(nums) - 1)


def main():
    solution = Solution()
    cases = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8], [-3,-1,-1,-1,-1,-1,]]  # sub array, near-empty array, entire array
    case_solutions = [6, 1, 23, -1]
    print("O(N^2)")
    for case in cases:
        print(f"Input: {case}")
        print(f"Output Expected: {case_solutions[cases.index(case)]}")
        result = solution.max_sub_array_nn(case)
        print(f"Output Actual: {result}")
        print(f"Correct: {result == case_solutions[cases.index(case)]}\n")
    print("=============================================\nO(N)")
    for case in cases:
        print(f"Input: {case}")
        print(f"Output Expected: {case_solutions[cases.index(case)]}")
        result = solution.max_sub_array_n(case)
        print(f"Output Actual: {result}")
        print(f"Correct: {result == case_solutions[cases.index(case)]}\n")
    # print("=============================================\nD&C approach")
    # for case in cases:
    #     print(f"Input: {case}")
    #     print(f"Output Expected: {case_solutions[cases.index(case)]}")
        # result = solution.max_sub_array_dnc(case)
        # print(f"Output Actual: {result}")
        # print(f"Correct: {result == case_solutions[cases.index(case)]}\n")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
