class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


# Chaining solution
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = [None] * self.size

    def calculate_hash_value(self, key):
        return key % self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        idx = self.calculate_hash_value(key)

        if self.table[idx] is None:
            self.table[idx] = ListNode(key, value)
        else:
            cur = self.table[idx]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)  # update
                    return
                if cur.next is None:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        idx = self.calculate_hash_value(key)

        cur = self.table[idx]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        idx = self.calculate_hash_value(key)

        cur = prev = self.table[idx]
        if not cur:
            return
        if cur.pair[0] == key:
            self.table[idx] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next
