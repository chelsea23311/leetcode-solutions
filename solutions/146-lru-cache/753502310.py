class LRUCache(object):
    class node():
        def __init__(self,key=0,value=0,prev=None,next=None):
            self.key=key
            self.value=value
            self.prev=prev
            self.next=next   

    def __init__(self, capacity):
        self.length=capacity
        self.map={}
        self.head,self.tail=self.node(),self.node()
        self.head.next=self.tail
        self.tail.prev=self.head
        """
        :type capacity: int
        """
    def to_head(self,key):
        nd = self.map[key]
        if nd == self.head.next:
            return
        nd.prev.next=nd.next
        nd.next.prev=nd.prev
        nd.next=self.head.next
        nd.next.prev=nd
        self.head.next=nd
    

    def get(self, key):
        if key in self.map:
            self.to_head(key)
            return self.map[key].value

        else:
            return -1
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        if key in self.map:
            self.map[key].value=value
            self.to_head(key)
        else:
            self.map[key]=self.node(key,value,self.head,self.head.next)
            self.to_head(key)
            if len(self.map)>self.length:
                old_node = self.tail.prev
                del self.map[old_node.key]
                old_node.prev.next=self.tail
                self.tail.prev=old_node.prev

        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)