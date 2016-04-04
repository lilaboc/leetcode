# https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode(object):
    def __init__(self, end = False):
        """
        Initialize your data structure here.
        """
        self.letters = {}
        self.end = end
        
    def insert(self, letter, end = False):
        node = self.letters.setdefault(letter, TrieNode(end))
        if not node.end and end:
            node.end = end
        return node
    
    def __contains__(self, item):
        return item in self.letters



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
        for index, value in enumerate(word):
            if index == len(word) - 1:
                current = current.insert(value, True)
            else:
                current = current.insert(value)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for index, value in enumerate(word):
            if value not in current:
                return False
            current = current.letters.get(value)
            if index == len(word) - 1:
                return current.end
        return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for index, value in enumerate(prefix):
            if value not in current:
                return False
            current = current.letters.get(value)
        return True
        

# Your Trie object will be instantiated and called as such:
#trie = Trie()
#trie.insert("somestring")
#print trie.search("somestring")
#print trie.search("somestringg")
#print trie.startsWith("some")
#print trie.startsWith("somestringg")
#print trie.startsWith("somestringga")
