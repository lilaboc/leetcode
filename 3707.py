# https://leetcode.com/problems/equal-score-substrings/description/

class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)
        # Try all possible split points
        for i in range(1, n):
            left = s[:i]
            right = s[i:]
            left_score = sum(ord(c) - ord('a') + 1 for c in left)
            right_score = sum(ord(c) - ord('a') + 1 for c in right)
            if left_score == right_score:
                return True
        return False


print(Solution().scoreBalance("ebd"))
print(Solution().scoreBalance("jhj"))
print(Solution().scoreBalance("adcb"))
print(Solution().scoreBalance("bace"))

