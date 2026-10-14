class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monoQueue = deque()
        maxList = []

        l = r = 0

        while r < len(nums):
            while monoQueue and (nums[monoQueue[-1]] < nums[r]):
                monoQueue.pop()
            monoQueue.append(r)

            if l > monoQueue[0]:
                monoQueue.popleft()

            if (r + 1) >= k:
                maxList.append(nums[monoQueue[0]])
                l += 1

            r += 1
        
        return maxList;
