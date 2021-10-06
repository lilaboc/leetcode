# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        parts = s.split()
        result = [""] * len(parts)
        for part in parts:
            result[int(part[-1]) - 1] = part[:-1]
        return " ".join(result)


print(Solution().sortSentence("is2 sentence4 This1 a3"))
