# Problem Link : https://leetcode.com/problems/trapping-rain-water/
# 42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        r = [0]*n
        r[-1] = height[-1]
        l = [0]*n
        l[0] = height[0]
        ans = 0
        
        for i in range(1, n):
            l[i] = max(l[i-1], height[i])
            r[n-1-i] = max(r[n-i], height[n-1-i])
        
        for i in range(n):
            ans += min(l[i], r[i]) - height[i]
        
        return ans