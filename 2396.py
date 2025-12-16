# https://leetcode.com/problems/strictly-palindromic-number/

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            if not isPalindromic(decimal_to_ternary(n, i)):
                return False
        return True

def isPalindromic(s: str) -> bool:
    return s == s[::-1]

def decimal_to_ternary(num, n):
    if num == 0:
        return '0'  # 直接返回'0'
    digits = []  # 用于存储余数
    while num > 0:
        num, remainder = divmod(num, n)  # 获得商和余数
        digits.append(str(remainder))    # 存储余数
    # 将余数列表反转并拼接成字符串，如果需要则添加负号
    result = ''.join(digits[::-1])
    return result

print(Solution().isStrictlyPalindromic(9))
print(Solution().isStrictlyPalindromic(4))
