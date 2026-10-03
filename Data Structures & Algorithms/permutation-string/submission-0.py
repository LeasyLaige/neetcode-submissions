class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub1_hash = {}
        sub2_hash = {}
        left = 0

        for char in s1:
            sub1_hash[char] = sub1_hash.get(char, 0) + 1

        for right, char in enumerate(s2):
            sub2_hash[char] = sub2_hash.get(char, 0) + 1

            if right - left + 1 > len(s1):
                sub2_hash[s2[left]] = sub2_hash.get(s2[left], 0) - 1
                if sub2_hash.get(s2[left], 0) == 0:
                    sub2_hash.pop(s2[left])
                left += 1

            if sub1_hash == sub2_hash:
                return True

        return False