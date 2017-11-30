# https://leetcode.com/problems/sentence-similarity/description/
from collections import defaultdict
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        pmap = defaultdict(set)
        for pair in pairs:
            a, b = pair
            pmap[a].add(b)
            pmap[b].add(a)


        if len(words1) != len(words2):
            return False
        for i in xrange(len(words1)):
            if words1[i] == words2[i]:
                continue
            elif words1[i] not in pmap or words2[i] not in pmap:
                return False
            elif words2[i] in pmap[words1[i]] and words1[i] in pmap[words2[i]]:
                continue
            else:
                return False
        return True

#print Solution().areSentencesSimilar(["great"], ["great"], [])
#print Solution().areSentencesSimilar(["an","extraordinary","meal"], ["one","good","dinner"], [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]])
