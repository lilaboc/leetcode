# https://leetcode.com/problems/repeated-dna-sequences/
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        else:
            seen = set()
            result = set()
            for i in xrange(0, len(s) - 9):
                dna = s[i: i + 10]
                #print dna
                if dna in seen:
                    result.add(dna)
                else:
                    seen.add(dna)
            return list(result)
#print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
#print Solution().findRepeatedDnaSequences("AAAAAAAAAA")
#print Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
