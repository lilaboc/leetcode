# https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.letters = {}
        self.end = False
        
    def insert(self, letter):
        node = self.letters.setdefault(letter, TrieNode())
        return node
    
    def __contains__(self, item):
        return item in self.letters

    def get(self, value):
        return self.letters.get(value)


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for  value in word:
            current = current.insert(value)
        current.end = True

    def search(self, word, care_end = True):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for value in word:
            if value not in current:
                return False
            current = current.get(value)
        return current.end if care_end else True
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.search(prefix, False)
        

# Your Trie object will be instantiated and called as such:
#trie = Trie()
#trie.insert("somestring")
#print trie.search("somestring")
#print trie.search("somestringg")
#print trie.startsWith("some")
#print trie.startsWith("somestringg")
#print trie.startsWith("somestringga")
