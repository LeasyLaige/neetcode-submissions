class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1

        largest = 0

        while left < right:
            current = min(heights[left], heights[right]) * (right - left)
            
            if largest < current:
                largest = current
            
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1

        return largest

            
            
