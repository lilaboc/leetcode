import string
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.s.add(word)
        self.length_set = set([len(word) for word in dict])
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.length_set:
            return False
        for i in self.mutate(word):
            if i in self.s:
                return True
        return False

        
    def mutate(self, word):
        for i in xrange(len(word)):
            for letter in string.lowercase:
                if letter != word[i]:
                    yield word[:i] + letter + word[i + 1:]


# Your MagicDictionary object will be instantiated and called as such:
#obj = MagicDictionary()
#obj.buildDict(["hello", "leetcode"])
#print(obj.search('hello'))
#print(obj.search('hhllo'))
#print(obj.search('hell'))
#print(obj.search('leetcoded'))
