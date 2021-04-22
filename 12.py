# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        result += 'M' * int(num / 1000)
        h = {1: "C", 2: "CC", 3:"CCC", 4: "CD", 5: "D", 6: "DC", 7:"DCC", 8:"DCCC", 9:"CM", 0:""}
        t = {1: "X", 2: "XX", 3:"XXX", 4: "XL", 5: "L", 6: "LX", 7:"LXX", 8:"LXXX", 9:"XC", 0:""}
        o = {1: "I", 2: "II", 3:"III", 4: "IV", 5: "V", 6: "VI", 7:"VII", 8:"VIII", 9:"IX", 0:""}
        num %= 1000
        result += h[int(num / 100)]
        num %= 100
        result += t[int(num / 10)]
        num %= 10
        result += o[int(num)]
        return result



print(Solution().intToRoman(3))
print(Solution().intToRoman(4))
print(Solution().intToRoman(9))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))