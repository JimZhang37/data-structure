
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LRU_Cache(object):
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.position = {}

    def set(self, key, value):
        if self.capacity <= 0:
            return
        if self.head is None:
            new_node = Node(key, value)
            self.head = new_node
            self.tail = self.head
            self.position[key] = new_node
        else:
            if key not in self.position:
                new_node = Node(key, value)
                if len(self.position) < self.capacity:
                    new_node.previous = self.tail
                    new_node.previous.next = new_node
                    self.tail = new_node
                    self.position[key] = new_node
                else:
                    old_node = self.head
                    self.head = self.head.next
                    self.head.previous = None
                    del self.position[old_node.value]
                    new_node.previous = self.tail
                    new_node.previous.next = new_node
                    self.tail = new_node
                    self.position[key] = new_node
            else:
                old_node = self.position[key]
                old_node.value = value
                if old_node is self.head:
                    self.head = self.head.next
                    self.head.previous = None
                    old_node.previous = self.tail
                    old_node.previous.next = old_node
                    old_node.next = Node
                elif old_node is self.tail:
                    return
                else:
                    pre = old_node.previous
                    next = old_node.next
                    pre.next = next
                    next.previous = pre
                    old_node.previous = self.tail
                    old_node.previous.next = old_node
                    old_node.next = None
                    self.tail = old_node


    def get(self, key):

        if key in self.position:
            old_node = self.position[key]
            if old_node is self.head:
                self.head = self.head.next
                if self.head is not None:
                    self.head.previous = None
                old_node.previous = self.tail
                old_node.previous.next = old_node
                old_node.next = None
                self.tail = old_node
            elif old_node is self.tail:
                return old_node.value
            else:
                pre = old_node.previous
                next = old_node.next
                pre.next = next
                next.previous = pre
                old_node.previous = self.tail
                old_node.previous.next = old_node
                old_node.next = None
                self.tail = old_node
            return old_node.value
        else:
            return -1

    def __repr__(self):
        str = "From its head: "
        i = 0
        node = self.head
        while node:
            str += f"{node.key}:{node.value}; "
            i += 1
            node = node.next
        str += f"The number of elements is {i}"

        str += "\nFrom its tail: "
        j = 0
        node1 = self.tail
        while node1:
            str += f"{node1.key}:{node1.value}; "
            j -= 1
            node1 = node1.previous
        str += f"The number of elements is {-j}"
        return str



# Test case 1
if __name__ == "__main__":

    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);


    print(our_cache.get(1))      # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    our_cache.set(7, 7)
    print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    our_cache.set(8, 8)
    print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    our_cache.set(6,6)
    print(our_cache.get(3))

    our_cache.set(2,2)
    print(our_cache.get(3))


    # Test case 2
    print(f'This is the second test case')
    our_cache1 = LRU_Cache(0)
    our_cache1.set(1, 1);
    our_cache1.set(2, 2);
    our_cache1.set(3, 3);
    our_cache1.set(4, 4);


    print(our_cache1.get(1))      # returns 1
    print(our_cache1.get(2))       # returns 2
    print(our_cache1.get(9))      # returns -1 because 9 is not present in the cache

    # Test case 3
    print(f'This is the third test case')
    our_cache2 = LRU_Cache(5)
    our_cache2.set(1, 1);
    our_cache2.set(2, 2);
    our_cache2.set(3, 3);
    our_cache2.set(4, 4);


    print(our_cache2.get(1))      # returns 1
    print(our_cache2.get(2))       # returns 2

    our_cache2.set(1, 11);
    our_cache2.set(2, 22);

    print(our_cache2.get(1))      # returns 11
    print(our_cache2.get(2))       # returns 22