class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None 


class MyHashMap:

    def __init__(self):
        self.map = [ListNode(0,0) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.map)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % len(self.map)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1 

    def remove(self, key: int) -> None:
        index = key % len(self.map)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)