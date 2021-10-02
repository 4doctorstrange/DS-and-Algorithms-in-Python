# Problem Link : https://leetcode.com/problems/largest-rectangle-in-histogram/
# 84. Largest Rectangle in Histogram

class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		st, ans = [], 0
		for i, ht in enumerate(heights+[0]):
			while st and heights[st[-1]] >= ht:
				h = heights[st.pop()] 
				w = i if not st else i-st[-1]-1
				ans = max(ans, w*h)
			st.append(i)
        
		return ans
