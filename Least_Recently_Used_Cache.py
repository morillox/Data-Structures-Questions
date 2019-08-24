import unittest
from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.maximum = capacity
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value

            return value
        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if self.maximum == 0:
            print("Cannot add new item to the cache: Initial capacity set to 0.")
            return

        if len(self.cache) == self.maximum:
            self.cache.popitem(last=False)  # Remove item in 'back' of order to make space.

        self.cache[key] = value


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =              Test cases.......              =
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class LRUCacheTesting(unittest.TestCase):

    def test_cache_one(self):
        our_cache = LRUCache(5)

        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)

        self.assertEqual(our_cache.get(1), 1)
        self.assertEqual(our_cache.get(2), 2)
        self.assertEqual(our_cache.get(9), -1)  # returns -1 because 9 is not present in the cache

        our_cache.set(5, 5)
        our_cache.set(6, 6)

        # Returns -1 because the cache reached it's capacity and 3 was the least recently used entry
        self.assertEqual(our_cache.get(3), -1)

    def test_cache_two(self):
        our_cache = LRUCache(3)

        our_cache.set(2, 4)
        our_cache.set(3, 9)

        # Cache list = [2, 3]
        self.assertEqual(our_cache.get(3), 9)

        # Cache list = [3,2]
        our_cache.set(4, 16)  # LRU is 2

        # Cache list = [4,3,2]
        self.assertEqual(our_cache.get(2), 4)  # LRU is 3

        # Cache list [2,4,3]
        our_cache.set(5, 25)  # LRU is 2

        # Cache list [5,2,4]
        self.assertEqual(our_cache.get(3), -1)

    def test_three(self):
        cache = LRUCache(2)

        cache.set(3, 6)  # Cache = [3]

        self.assertEqual(cache.get(3), 6)

        cache.set(4, 8)  # Cache = [4, 3]

        self.assertEqual(cache.get(3), 6)  # Cache [3,4]

        cache.set(5, 10)  # Cache [5,3]

        self.assertEqual(cache.get(4), -1)  # Cache [5,3]

    def test_zeroed_cache(self):
        cache = LRUCache(0)

        cache.set(4, 16)  # Cache = []

        self.assertEqual(cache.get(4), -1)

        cache.set(5, 25)  # Cache = []
        self.assertEqual(cache.get(5), -1)

    def test_single_lru_cache(self):
        cache = LRUCache(1)

        cache.set(4, 16)  # Cache = [4]
        self.assertEqual(cache.get(4), 16)

        cache.set(5, 25)  # Cache = [5]
        self.assertEqual(cache.get(5), 25)
        self.assertEqual(cache.get(4), -1)

    def test_duplicate_entries(self):
        cache = LRUCache(6)

        cache.set(4, 16)  # Cache = [4]
        cache.set(5, 25)  # Cache = [4, 5]
        cache.set(3, 9)  # Cache = [3, 4,5]

        self.assertEqual(cache.get(3), 9)  # No change in cache order.

        cache.set(2, 4)  # Cache = [2, 3, 4]
        cache.set(4, 91)  # Cache = [4, 2, 3]

        self.assertEqual(cache.get(4), 91)  # Cache[4] should be equal to the new value, not 16
        pass


if __name__ == '__main__':
    unittest.main()

