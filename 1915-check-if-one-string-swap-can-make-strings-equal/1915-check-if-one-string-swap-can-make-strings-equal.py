class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)

        if len(diffs) != 2:
            return False

        i, j = diffs[0], diffs[1]
        
        return s1[i] == s2[j] and s1[j] == s2[i]        