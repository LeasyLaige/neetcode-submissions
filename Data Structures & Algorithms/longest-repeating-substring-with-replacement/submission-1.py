class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        right = 0

        subHash = {}
        longestSubLength = 0;

        for i in range(n):
            char = s[i]

            subHash[char] = subHash.get(char, 0) + 1
            
            windowLength = right - left + 1
            subWindow = windowLength - subHash.get(max(subHash, key=subHash.get), 0)

            while subWindow > k:
                subHash[s[left]] = subHash.get(s[left], 0) - 1
                left += 1
                windowLength = right - left + 1
                subWindow = windowLength - subHash.get(max(subHash, key=subHash.get), 0)

            if windowLength > longestSubLength:
                longestSubLength = windowLength

            right += 1

        
        return longestSubLength



        


        