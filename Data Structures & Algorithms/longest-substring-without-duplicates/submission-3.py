class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subHashMap = {}
        subLength = 0

        for char in s:
            if char not in subHashMap:
                subHashMap[char] = subHashMap.get(char, 0) + 1
            elif char in subHashMap:
                if len(subHashMap) > subLength:
                    subLength = len(subHashMap)
                
                for key in list(subHashMap.keys()):
                    subHashMap.pop(key)
                    if key == char:
                        break
                    
                subHashMap[char] = subHashMap.get(char, 0) + 1

            if len(subHashMap) > subLength:
                subLength = len(subHashMap)


        return subLength