# https://leetcode.com/problems/ransom-note/#/description
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_map = Counter(magazine)
        for i in ransomNote:
            if i in magazine_map:
                magazine_map[i] -= 1
                print magazine_map
                if magazine_map[i] < 0:
                    return False
            else:
                return False

        return True
#print Solution().canConstruct('aa', 'aab')
#print Solution().canConstruct('a', 'b')
#print Solution().canConstruct('aa', 'ab')
#print Solution().canConstruct('aa', 'aab')
