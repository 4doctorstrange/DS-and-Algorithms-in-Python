# Problem Link : https://leetcode.com/problems/two-sum/
# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i<len(nums):
            required = target-nums[i]
            try:
                second = nums.index(required, i+1)
                break
            except ValueError:
                i+=1
                
        return (i, second)
