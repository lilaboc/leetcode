# https://leetcode.com/problems/add-and-search-word-data-structure-design/
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


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for  value in word:
            current = current.insert(value)
        current.end = True

    def search(self, word, root = None):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root if not root else root
        for index, value in enumerate(word):
            if value == '.':
                for i in current.letters:
                    node = current.get(i)
                    if self.search(word[index + 1:], node):
                        return True
                return False
            elif value not in current:
                return False
            current = current.get(value)
        return current.end 
        

        

# Your WordDictionary object will be instantiated and called as such:
#wordDictionary = WordDictionary()
#wordDictionary.addWord("word")
#print wordDictionary.search("pattern")
#print wordDictionary.search("word")
#print wordDictionary.search(".ord")
#print wordDictionary.search("wo..")
#print wordDictionary.search("wo..d")
