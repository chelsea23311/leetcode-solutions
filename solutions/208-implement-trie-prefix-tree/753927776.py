class Trie(object):

    def __init__(self):
        self.s=''
        self.hashmap={}
    def insert(self, word):
        self.hashmap[word]=1
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        if word in self.hashmap:
            return True
        else:
            return False
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        length=len(prefix)
        for key in self.hashmap:
            if key[0:length]==prefix:
                return True
        return False
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)