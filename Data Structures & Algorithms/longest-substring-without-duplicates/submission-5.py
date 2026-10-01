class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subHashMap = {}
        subLength = 0

        for char in s:
            if char not in subHashMap:
                subHashMap[char] = 1
            else:                
                for key in list(subHashMap.keys()):
                    subHashMap.pop(key)
                    if key == char:
                        break
                    
                subHashMap[char] = 1

            if len(subHashMap) > subLength:
                subLength = len(subHashMap)


        return subLength