class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words_set = set(words)
        result = []
        for word in words:
            if self.self_built(word, words_set):
                result.append(word)
        return max(sorted(result), key = len)
            
    def self_built(self, word, words_set):
        for i in xrange(1, len(word)):
            if word[:i] not in words_set:
                return False
        return True


#print Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
#print Solution().longestWord(["w","wo","wor","worl", "world"])
