# https://leetcode.com/problems/reverse-prefix-of-word/


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            index = word.index(ch)
            return ''.join(reversed(word[:index + 1])) + word[index + 1:]
        except ValueError:
            return word


print(Solution().reversePrefix("abcdefd", 'd'))