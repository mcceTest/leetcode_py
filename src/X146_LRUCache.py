'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''



class LRUCache(object):
    class DNode(object):
        def __init__(self, key, val, pre=None, nxt=None):
            self.key = key
            self.val = val
            self.pre = pre
            self.nxt = nxt

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.count = 0
        self.nodeMap = {}

    def moveToHead(self, node):
        if node == self.head:
            return

        if node == self.tail:
            self.tail = node.pre

        node.pre.nxt = node.nxt
        if node.nxt:
            node.nxt.pre = node.pre

        node.pre = None
        node.nxt = self.head
        self.head.pre = node

        self.head = node

    def removeTail(self):
        curTail = self.tail
        self.tail = curTail.pre
        if self.tail:
            self.tail.nxt = None
        curTail.pre = None
        curTail.nxt = None
        
        self.count -= 1
        del self.nodeMap[curTail.key]

    def addToHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.nxt = self.head
            self.head.pre = node
            self.head = node

        self.count += 1
        self.nodeMap[node.key] = node

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.moveToHead(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.moveToHead(node)
        else:
            if self.count == self.capacity:
                self.removeTail()
            node = LRUCache.DNode(key, value)
            self.addToHead(node)
            



    @staticmethod
    def main():
        cache = LRUCache(1)
        cache.put(2, 1)
        print(cache.get(2))
        cache.put(3, 2)
        print(cache.get(2))
        print(cache.get(3))
        

if __name__ == "__main__":
    LRUCache.main()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)