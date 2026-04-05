class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stk_i, stk_h = stack.pop()
                maxArea =  max(maxArea, stk_h * (i - stk_i))
                start = stk_i
            
            stack.append((start, h))

        while stack:
            stk_i, stk_h = stack.pop()
            maxArea = max(maxArea, stk_h * (len(heights)-stk_i))

        return maxArea
