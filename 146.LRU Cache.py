class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dummy = Node()
        self.node_to_prev = {}
        self.tail = self.dummy #Initially, the dummy node is the tail node as there is no other node.

    def pop_top(self):
        head = self.dummy.next
        del self.node_to_prev[head.key]
        self.dummy.next = head.next
        self.node_to_prev[head.next.key] = self.dummy

    def set_new_node(self, node):
        self.node_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def refresh_old_node(self, prev):
        node = prev.next
        if node == self.tail:
            return None

        prev.next = node.next
        self.node_to_prev[node.next.key] = prev
        node.next = None

        self.set_new_node(node)

    def get(self, key):
        if key not in self.node_to_prev:
            return -1

        prev = self.node_to_prev[key]
        curNode = prev.next

        self.refresh_old_node(prev)
        return curNode.val
        

    def put(self, key, value):
        if key in self.node_to_prev:
            self.refresh_old_node(self.node_to_prev[key])
            self.node_to_prev[key].next.val = value
            return None

        self.set_new_node(Node(key, value))
        if len(self.node_to_prev) > self.capacity:
            self.pop_top()
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
