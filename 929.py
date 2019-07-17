# https://leetcode.com/problems/unique-email-addresses/
from typing import List
import re

pattern = re.compile(r'(?P<local>[^\+@]*)\+?[^@]*@(?P<domain>.*)')
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        results = set()
        for email in emails:
            m = re.search(pattern, email)
            if m:
                local_name = m.group('local').replace('.', '')
                domain = m.group('domain')
                results.add(f'{local_name}@{domain}')
        return len(results)


print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
                    
