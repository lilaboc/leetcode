#  https://leetcode.com/problems/convert-date-to-binary/description/

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(decimal_to_ternary(int(x), 2) for x in date.split("-"))



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


print(Solution().convertDateToBinary("2080-02-29"))
print(Solution().convertDateToBinary("1900-01-01"))
