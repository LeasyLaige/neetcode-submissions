class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) <= 0 or target == None:
            return []

        seen = {}

        result = []

        for index, value in enumerate(nums):
            need = target - value

            if need in seen:
                result = [seen.get(need), index]
                return result
            else:
                seen[value] = index
        
        return []