
# Given an array of points where points[i] = [xi, yi] represents a point on the 
# X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance 
# (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique 
# (except for the order that it is in).
# https://leetcode.com/problems/k-closest-points-to-origin/description/
import heapq
import os
import sys
import math
import time
import typing
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # https://www.iditect.com/program-example/python--get-closest-coordinate-in-2d-array.html
        min_heap = []
        print(points)
        for point in points:
            print(f"{point}")
            distance_to_origin = (point[0]**2) + (point[1]**2)
            heapq.heappush(min_heap, (distance_to_origin, point))
        return heapq.nsmallest(k, distance_to_origin)

def test(cases, solutions, function, show_answer=False):
    correct = 0
    for case in cases:
        print(case)
        if show_answer: 
            print(f"Input: {cases}")
        result = function(case[0], [1])
        if show_answer: 
            print(f"Output Actual: {result}")
        if show_answer: 
            print(f"Output Expected: {solutions[cases.index(case)]}")
        correct = correct+1 if result == solutions[cases.index(case)] else correct

def main():
    solution = Solution()
    cases = [ ([[3,3],[5,-1],[-2,4]], 2), ([[1,3],[-2,2]], 1)]
    case_solutions = [ [[3,3],[-2,4]], [[-2,2]] ]
    
    
    print("HEAP")
    test(cases, case_solutions, solution.kClosest, show_answer=False)
    
    


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()