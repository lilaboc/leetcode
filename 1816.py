# https://leetcode.com/problems/truncate-sentence/


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        r = []
        space = 0
        for i in s:
            if i == " ":
                space += 1
                if space == k:
                    break
            r.append(i)
        return "".join(r)



print(Solution().truncateSentence("Hello how are you Contestant", 4))
print(Solution().truncateSentence("What is the solution to this problem", 4))
