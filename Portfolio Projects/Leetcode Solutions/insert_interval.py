# Author: Stefan DeWolfe
# Date: 6/2024
# You are given an array of non-overlapping intervals "intervals" where intervals[i] = [start_i, end_i] represent the
# start and the end of the ith interval and intervals is sorted in ascending order by start_i.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and intervals
# still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

# Constraints:
#     0 <= intervals.length <= 104                      between 0 and 104 inclusively.
#     intervals[i].length == 2                          Always tuples
#     0 <= starti <= endi <= 105                        start_i is always less then end_i, see above. End_i is EXCLUSIVE
#     intervals is sorted by starti in ascending order. see above
#     newInterval.length == 2                           Always tuples, again
#     0 <= start <= end <= 105                          see above

import os
import sys
import typing
from typing import List


class Solution:
    def insert2(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        result_interval = []
        starting_interval = intervals[0]
        starting_interval_index = 0
        ending_interval = None
        ending_interval_index = 0
        # Find starting interval, add others to the front of the new list of intervals
        for interval in intervals:
            if interval[0] <= new_interval[0] <= interval[1]:
                starting_interval = interval
                starting_interval_index = intervals.index(interval)
                break
            else:
                result_interval.append(interval)
        # Find ending interval, ignore the rest
        # start from the next one after the starting interval
        for i in range(intervals.index(starting_interval)+1, len(intervals)):
            if intervals[i][0] <= new_interval[1] <= intervals[i][1]:
                ending_interval = intervals[i]
                ending_interval_index = intervals.index(ending_interval)
                break
        # modify the starting interval if needed
        starting_interval[1] = new_interval[1]
        if ending_interval and starting_interval[1] == ending_interval[0]:
            starting_interval[1] = ending_interval[1]
            ending_interval = None
        result_interval.append(starting_interval)
        if ending_interval:
            result_interval.append(ending_interval)
        else:
            ending_interval_index = starting_interval_index
            ending_interval = starting_interval
        # Add the rest into the result interval list at the end...
        for i in range(ending_interval_index+1, len(intervals)):
            if intervals[i][0] > ending_interval[1]:
                result_interval.append(intervals[i])
        return result_interval
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 1:
            if intervals[0][0] <= newInterval[1] and newInterval[1] <= intervals[0][1]:
                return intervals
            elif newInterval[0] >= intervals[0][0] and newInterval[1] < intervals[0][1]:

        intervals.insert(0, newInterval)
        intervals.sort()
        start_i = 0
        while start_i < len(intervals)-1:
            print(f" {start_i} {len(intervals) - 1}")
            print(f" {intervals[start_i][0]},{intervals[start_i+1][0]}")
            if intervals[start_i][1] >= intervals[start_i+1][0]:
                intervals[start_i][1] = intervals[start_i+1][1]
                intervals.remove(intervals[start_i+1])
            if intervals[start_i][1] >= intervals[start_i + 1][1]:
                intervals.remove(intervals[start_i+1])
            if intervals[start_i][1] >= intervals[start_i + 1][0]:
                intervals[start_i][1] = intervals[start_i + 1][1]
                intervals.remove(intervals[start_i + 1])
            start_i += 1
        return intervals


def test(intervals, new_intervals, solutions, method):
    for interval in intervals:
        new_interval = new_intervals[intervals.index(interval)]
        print(f"Input: {interval} | {new_interval}")
        print(f"Output Expected: {solutions[intervals.index(interval)]}")
        result = method(interval, new_interval)
        print(f"Output Actual: {result}")
        print(f"Correct: {result == solutions[intervals.index(interval)]}\n")
        print("=============================================")


def main():
    solution = Solution()
    intervals = [[[1,3],[6,9]] ,[[1,2],[3,5],[6,7],[8,10],[12,16]], ]  # sub array, near-empty array, entire array
    new_intervals = [[2,5], [4,8]]
    intervals_solutions = [[[1,5],[6,9]], [[1,2],[3,10],[12,16]]]

    #print("O(N^2) un-optimized")
    #test(intervals, new_intervals, intervals_solutions, solution.insert2 )
    print("O(N) more-optimized")
    test(intervals, new_intervals, intervals_solutions, solution.insert )


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
