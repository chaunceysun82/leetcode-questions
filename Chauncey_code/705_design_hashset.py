class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2069
        self.hash_table = [Bucket() for _ in range(self.key_space)]

    def add(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].insert(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].if_exists(key)


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Bucket:
    def __init__(self):
        self.dummy_head = ListNode(-1)

    def insert(self, new_value):
        # inset to head if not exist
        if not self.if_exists(new_value):
            new_node = ListNode(new_value, self.dummy_head.next)
            self.dummy_head.next = new_node

    def delete(self, value):
        prev = self.dummy_head
        cur = self.dummy_head.next
        while cur:
            if cur.value == value:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def if_exists(self, value):
        cur = self.dummy_head.next
        while cur:
            if cur.value == value:
                return True
            cur = cur.next

        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)