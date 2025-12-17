# https://leetcode.com/problems/sort-vowels-in-a-string/description/

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        for i in s:
            if i in 'aeiouAEIOU':
                vowels.append(i)
        vowels.sort(reverse=True)
        result = []
        for i in s:
            if i in 'aeiouAEIOU':
                result.append(vowels.pop())
            else:
                result.append(i)
        return ''.join(result)


print(Solution().sortVowels("lEetcOde"))
