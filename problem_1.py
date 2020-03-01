class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.capacity = capacity
        self.items = {}
        self.list = []
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.items:
            self.list.remove(key)
            self.list.append(key)
            return self.items[key]
        else:
            return -1


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.items:
            self.items[key] = value
            self.list.remove(key)
            self.list.append(key)
        else:
            if len(self.list) < self.capacity:
                self.items[key] = value
                self.list.append(key)
            else:
                self.items.pop(self.list[0])
                self.list.pop(0)
                self.items[key] = value
                self.list.append(key)
        print(self.list)



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

