# https://leetcode.com/problems/defanging-an-ip-address/
import functools
class Solution:
    @functools.lru_cache(maxsize=128, typed=False)
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
                    
