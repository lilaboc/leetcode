# https://leetcode.com/problems/count-primes/
from typing import List, Generator


class Solution:
    def countPrimes(self, n: int) -> int:
        return sum(1 for i in self._primes_sieve(n) if i)

    def _primes_sieve(self, limit: int) -> Generator[bool, None, None]:
        if limit == 0 or limit == 1:
            return
        a = [True] * limit  # Initialize the primality list
        a[0] = a[1] = False

        for (i, isprime) in enumerate(a):
            if isprime:
                yield i
                for n in range(i * i, limit, i):  # Mark factors non-prime
                    a[n] = False


print(Solution().countPrimes(10))
