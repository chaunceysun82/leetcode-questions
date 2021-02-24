# Method 1: OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)

        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value



# Method 2, hashmap + linkedlist

class LinkedNode:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.dummy_head = LinkedNode()
        self.dummy_tail = LinkedNode()
        self.cache = {}
        self.capacity = capacity
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head


    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_end(self, node):

        node.prev = self.dummy_tail.prev
        self.dummy_tail.prev = node
        node.prev.next = node
        node.next = self.dummy_tail

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove_node(node)
        self._add_to_end(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_end(node)
            return
        elif len(self.cache) == self.capacity:
            lru_node = self.dummy_head.next
            self._remove_node(lru_node)
            del self.cache[lru_node.key]
        new_node = LinkedNode(key, value)
        self.cache[key] = new_node
        self._add_to_end(new_node)