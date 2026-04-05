class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev =  self.right, self.left
        
    def update(self, key):
        node = self.cache[key]
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev

        recent_node = self.right.prev
        recent_node.next = node
        node.prev = recent_node
        node.next = self.right
        self.right.prev = node
          

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.update(key)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key].val = value
            self.update(key)
        
        else:
            if len(self.cache) == self.capacity:
                self.cache.pop(self.left.next.key)
                next_node = self.left.next.next
                self.left.next = next_node
                next_node.prev = self.left



            node = Node(key, value)
            self.cache[key] = node

            prev_node = self.right.prev
            prev_node.next = node
            node.prev = prev_node
            node.next = self.right
            self.right.prev = node


        
