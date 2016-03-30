# https://leetcode.com/problems/compare-version-numbers/

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        cur = 0
        len1 = len(v1)
        len2 = len(v2)
        while True:
            if cur >= len1 and cur >= len2:
                return 0
            elif cur >= len1 and int(v2[cur]) != 0:
                return -1
            elif cur >= len2 and int(v1[cur]) != 0:
                return 1
            elif cur >= len1 or cur >= len2:
                cur += 1
            else:
                if int(v1[cur]) > int(v2[cur]):
                    return 1
                elif int(v1[cur]) < int(v2[cur]):
                    return -1
                else:
                    cur += 1
#print Solution().compareVersion('0', '1')
