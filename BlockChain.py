import hashlib
import datetime


class Blockchain:
    def __init__(self):
        self.tail = None
        self.length = 0

    def add_block(self, data):
        timestamp = datetime.datetime.now()
        prev_hash = self.tail.hash if self.tail else 0

        block = Block(timestamp, data, prev_hash)

        self.tail = block

    def __len__(self):
        return self.length

    def __str__(self):
        return f'Leading Blockchain Hash: {self.tail.hash}'


class Block(object):

    def __init__(self, timestamp, data, previous_hash):
        """

        :param timestamp:
        :param data:
        :param previous_hash:
        """

        self.timestamp = timestamp

        self.data = data
        self.previous_hash = previous_hash

        self.hash = self.calc_hash()

    def __str__(self):
        return f'Block hash: {self.hash}'

    def calc_hash(self):
        """

        :rtype: str
        """
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()