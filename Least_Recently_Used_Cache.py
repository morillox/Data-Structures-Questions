class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cacheSize = capacity
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

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =              Test cases.......              =
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def test_One():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    assert our_cache.get(1) == 1  # Returns 1
    assert our_cache.get(2) == 2  # Returns 2
    assert our_cache.get(9) == -1  # Returns -1

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    assert our_cache.get(3) == -1   # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

def test_Two():
    our_cache = LRU_Cache(3)
    our_cache.set(2, 4)
    our_cache.set(3, 9)

    assert our_cache.get(3) == 9
    # Order list = [3, 2]

    our_cache.set(4, 16)
    # Order list = [4, 3, 2]

    assert our_cache.get(2) == 4
    # Order list = [2, 4, 3]

    our_cache.set(5, 25)
    # Order list = [5, 2, 4]

    assert our_cache.get(3) == -1

def test_Three():
    cache = LRU_Cache(2)

    cache.set(3, 6)
    # Order = [3]

    assert cache.get(3) == 6

    cache.set(4, 8)
    # Order = [4, 3]

    assert cache.get(3) == 6
    # Order [3,4]

    cache.set(5, 10)
    # Order [5,3]

    assert cache.get(4) == -1
    # Order [5,3]

test_One()
test_Two()
test_Three()