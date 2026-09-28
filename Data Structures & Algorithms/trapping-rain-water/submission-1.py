class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1

        maxLeft = height[left]
        maxRight = height[right]

        finalVolume = 0;


        while left < right:
            leftVal = maxLeft - height[left]
            rightVal = maxRight - height[right]

            if leftVal > 0:
                finalVolume += leftVal
            if rightVal > 0:
                finalVolume += rightVal

            if maxLeft > maxRight:
                right -= 1
            else:
                left += 1
                
            if height[left] > maxLeft:
                maxLeft = height[left]
            elif height[right] > maxRight:
                maxRight = height[right]

        return finalVolume
