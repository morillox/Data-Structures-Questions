import datetime
import hashlib
import unittest

from collections import deque


class Blockchain:
    def __init__(self):
        self.tail: Block = None
        self.queue = deque()
        self.size = 0

    def __str__(self):
        return f'Leading Blockchain Hash: {self.tail.hash}'

    def __len__(self):
        return self.size

    def add_block(self, data):
        timestamp = datetime.datetime.utcnow()
        prev_hash = self.tail.hash if self.tail else 0

        block = Block(timestamp, data, prev_hash)
        self.tail = block
        self.size += 1

    def get_latest_block(self):
        return self.tail


class Block(object):

    def __init__(self, timestamp, data, previous_hash):
        """

        :param timestamp:
        :param data:
        :param previous_hash:
        """

        self.timestamp: datetime.datetime = timestamp

        self.data: str = data
        self.previous_hash = previous_hash

        self.hash = self.calc_hash()

    def __str__(self):
        return f'Block hash: {self.hash}'

    def calc_hash(self):
        """

        :rtype: str
        """
        sha = hashlib.sha256()
        sha.update(
            str(self.data).encode('utf-8')
        )
        return sha.hexdigest()


class EncryptionTest(unittest.TestCase):
    def test_encrypts_one(self):
        chain = Blockchain()

        chain.add_block(3.1415)
        block1: Block = chain.get_latest_block()

        chain.add_block(6.1920)
        block2: Block = chain.get_latest_block()

        self.assertEqual(block1.hash, block2.previous_hash)

    def test_encrypts_two(self):
        chain = Blockchain()

        chain.add_block("hello there")
        block1: Block = chain.get_latest_block()

        chain.add_block("general Kenoby")
        block2: Block = chain.get_latest_block()

        chain.add_block("You're a bold one")
        block3: Block = chain.get_latest_block()

        self.assertEqual(block3.previous_hash, block2.hash)
        self.assertEqual(block2.previous_hash, block1.hash)
        self.assertEqual(block1.previous_hash, 0)

    def test_encrypts_three(self):
        chain = Blockchain()
        test_data = "this is a test case"

        chain.add_block(test_data)
        block = chain.get_latest_block()

        test_data_hashing = hashlib.sha256(
            test_data.encode('utf-8')
        ).hexdigest()

        self.assertEqual(block.hash, test_data_hashing)
        self.assertEqual(block.previous_hash, 0)


if __name__ == '__main__':
    unittest.main()
