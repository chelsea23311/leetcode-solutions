class Trie(object):

    def __init__(self):
        self.root=self.node()

        
    class node:
        def __init__(self,char=' '):
            self.isEnd=False
            self.char=char
            self.children={}

    def insert(self, word):
        cur=self.root
        for c in word:
            if c not in cur.children:
                new=self.node(c)
                cur.children[c]=new
            cur=cur.children[c]
        cur.isEnd=True
        """
        :type word: str
        :rtype: None
        """
    def search(self, word):
        cur=self.root
        for c in word:
            if c in cur.children:
                cur=cur.children[c]
            else:
                return False
        return True if cur.isEnd else False
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        cur=self.root
        for c in prefix:
            if c in cur.children:
                cur=cur.children[c]
            else:
                return False
        return True
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)