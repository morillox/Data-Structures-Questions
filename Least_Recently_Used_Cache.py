class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cacheSize = 5
        self.cache = {}
        self.recentUsed = []

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.recentUsed:
            self.recentUsed.remove(key)
        if key in self.cache.keys():
            self.recentUsed.insert(0, key)
            return self.cache.get(key)
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        self.recentUsed.insert(0, key)
        self.cache[key] = value
        self.remove_overflow()

    def remove_overflow(self):
        if len(self.cache) > self.cacheSize:
            lru = self.recentUsed.pop()
            self.cache.pop(lru)


# Test.......
our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

assert our_cache.get(1) == 1  # Returns 1
assert our_cache.get(2) == 2  # Returns 2
assert our_cache.get(9) == -1  # Returns -1

our_cache.set(5, 5)
our_cache.set(6, 6)

assert our_cache.get(3) == -1   # returns -1 because the cache reached it's capacity and 3 was the least recently used entry