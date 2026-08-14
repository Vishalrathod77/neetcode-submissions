class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1 

        for chars in t:
            if chars not in counts:
                return False
            else:
                counts[chars] -= 1  

            if counts[chars] < 0:
                return False
        return True      