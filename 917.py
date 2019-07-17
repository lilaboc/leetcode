# https://leetcode.com/problems/reverse-only-letters/
import string
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if len(S) <= 1:
            return S
        low = 0
        high = len(S) - 1
        result = list(S)
        letters = string.ascii_uppercase + string.ascii_lowercase
        while True:
            while True:
                if low >= high or S[low] in letters:
                    break
                else:
                    low += 1
            while True:
                if high <= low or S[high] in letters:
                    break
                else:
                    high -= 1
            #print(low, high)
            result[low] , result[high] = result[high], result[low]
            low += 1
            high -= 1
            if low >= high:
                return ''.join(result)

print(Solution().reverseOnlyLetters(''))
print(Solution().reverseOnlyLetters('-'))
print(Solution().reverseOnlyLetters('a'))
print(Solution().reverseOnlyLetters('ab-cd'))
print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))
print(Solution().reverseOnlyLetters("?6C40E"))
