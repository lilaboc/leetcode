# https://leetcode.com/problems/sentence-similarity-ii/description/
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        m = {}
        for pair in pairs:
            # if two words are already seen, need to merge existing sets
            if all(map(m.has_key, pair)):
                s = m[pair[0]].union(m[pair[1]])
                for word in s:
                    m[word] = s
            # if only one seen, need to merge new words into the existing set
            elif any(map(m.has_key, pair)):
                #existing key
                s = m[filter(m.has_key, pair)[0]]
                s.add(pair[0])
                s.add(pair[1])
                for word in pair:
                    m[word] = s
            # never seen, new set
            else:
                s = set(pair)
                for word in pair:
                    m[word] = s
        for i in xrange(len(words1)):
            if words1[i] == words2[i]:
                continue
            elif words1[i] not in m or words2[i] not in m:
                return False
            elif words2[i] in m[words1[i]]:
                continue
            else:
                return False
        return True




#print Solution().areSentencesSimilarTwo(["great", "acting", "skills"], ["fine", "drama", "talent"],  [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]])
#print Solution().areSentencesSimilarTwo(["great"],  ['great'], [])
#print Solution().areSentencesSimilarTwo(["great"],  ['doubleplus', "good"], [])
