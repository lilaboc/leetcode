# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

def digits(n):
    r = []
    while n != 0:
        r.append(n % 10)
        n //= 10
    return r[::-1]


def product(n):
    r = 1
    for i in n:
        r *= i
    return r


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = digits(n)
        return product(n) - sum(n)


print(Solution().subtractProductAndSum(234))
print(Solution().subtractProductAndSum(4421))




