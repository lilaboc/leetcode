# https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = set('aeiouAEIOU')
        result = []
        words = S.split()
        for i, v in enumerate(words):
            if v[0] in vowels:
                for l in v:
                    result.append(l)
            else:
                for l in v[1:]:
                    result.append(l)
                result.append(v[0])
            result.append('m')
            result.append('a')
            for _ in range(i + 1):
                result.append('a')
            if i != len(words) - 1:
                result.append(' ')
        return "".join(result)
    

print(Solution().toGoatLatin("The quick brown fox jumped over the lazy dog"))
                



