# https://leetcode.com/problems/license-key-formatting/#/description
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        dash_count = S.count('-')
        first = (len(S) - dash_count) % K
        count = 0
        result = []
        part = ''
        for i in S:
            if i == '-':
                continue
            if count == first or (count - first) % K == 0:
                if part != '':
                    result.append(part.upper())
                part = i
                count += 1
            else:
                part += i
                count += 1
        result.append(part.upper())
        return "-".join(result)

#print Solution().licenseKeyFormatting("2-4A0r7-4k", 3)
#print Solution().licenseKeyFormatting("2-4A0r7-4k", 4)
