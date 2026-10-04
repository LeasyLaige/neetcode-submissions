class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "": 
            return ""
        
        targetHash = {}
        currentHash = {}

        for char in t:
            targetHash[char] = targetHash.get(char, 0) + 1

        result = [-1, -1]
        resultLen = float("inf")

        have = 0
        need = len(targetHash)

        left = 0

        for right, char in enumerate(s): 
            currentHash[char] = currentHash.get(char, 0) + 1

            if char in targetHash and currentHash[char] == targetHash[char]:
                have += 1

            while need == have:
                currentLen = right - left + 1

                if currentLen < resultLen:
                    resultLen = currentLen
                    result = [left, right]

                leftChar = s[left]
                currentHash[leftChar] = currentHash.get(leftChar, 0) - 1

                if s[left] in targetHash and currentHash[s[left]] < targetHash[s[left]]:
                    have -= 1
                
                left += 1


        shortestSub = ""

        if resultLen == float('inf'):
            return ""

        for i in range(result[0], result[1] + 1):
            shortestSub += s[i]
                    
        return shortestSub
