import sys


class Node:
    def __init__(self, left=None, right=None, char: str = None, frequency: int = None):
        self.left = left
        self.right = right
        self.char = char
        self.frequency = frequency

    def __str__(self):
        if self.char is None:
            return "Null node with freq: %s" % self.frequency
        return "Char node with char: %s and freq: %s" % (self.char, self.frequency)


def tree_traversal(node, pre_string='', cache=None):
    """
    Creates a Tree traversal using the Tree created previously.
    It works by creating a dictionary, and using that reference throughout the function.

    As Python creates a reference to an list and dict objects, if one modifies it within the function
    it's also modified outside of it.

    By modifying the reference to the dictionary passed throughout the function,
    we can update the path for each node, and return it in the end.

    :param node: Root node used to traverse the tree.
    :param pre_string: Path taken to that node. Each level appends a 0 if it took a left, 1 otherwise
    :param cache: Dictionary containing the path for each of the strings that have been traversed.
    :return: cache dictionary/
    """
    if node is None:
        return None
    if cache is None:
        cache = dict()
    if node.char is not None:
        cache[pre_string] = node.char

    # Traversing the tree to the left, append a 0 to the path taken, and give a reference to the cache.
    tree_traversal(node.left, pre_string=pre_string + "0", cache=cache)

    # Traversing the tree to the right, append a 1 to the path taken, and give a reference to the cache.
    tree_traversal(node.right, pre_string=pre_string + "1", cache=cache)

    return cache


def huffman_encoding(data: str):
    """
    :param data: String to be encoded using the Huffman encoding algorithm.
    :return
    """
    if not data:
        return '0', None

    try:
        data = data.lower()
    except ValueError:
        print("Invalid data, cannot encode this data!!")

    from collections import Counter

    # Creates a dictionary with each letter being a key,
    # and the corresponding value how many times it appears on the string.
    frequency = Counter(data)

    # Create an ordered list containing each letter and its frequency in ascending order.
    ordered_frequency = sorted(frequency.items(), key=lambda kv: kv[1])  # List[(key,value)]

    # Create nodes for all the characters
    ordered_nodes = [Node(char=pair[0], frequency=pair[1]) for pair in ordered_frequency]  # type: list[Node]

    while len(ordered_nodes) > 1:
        node = Node(
            left=ordered_nodes[0],
            right=ordered_nodes[1],
            frequency=ordered_nodes[0].frequency + ordered_nodes[1].frequency
        )
        ordered_nodes.pop(0)
        ordered_nodes.pop(0)

        # Insert back into ordered_nodes
        ordered_nodes.append(node)
        ordered_nodes = sorted(ordered_nodes, key=lambda v: v.frequency)

    # Create a cache using the Tree created previously.
    cache = tree_traversal(ordered_nodes[0])
    inv_map = {v: k for k, v in cache.items()}
    encoded = ""
    for char in data:
        encoded += inv_map[char]

    return encoded, cache


def huffman_decoding(data, tree):
    if not tree and data == "0":
        return ""

    sentence = ""
    c_index = 0
    while True:
        c_range = 1

        while True:
            try:
                word = data[c_index:c_index + c_range]
                sentence += tree[word]
                break
            except KeyError:
                c_range += 1
        if c_index + c_range == len(data):
            break
        c_index += c_range
    return sentence


if __name__ == "__main__":
    codes = {}

    # a_great_sentence = "this is an example of a huffman tree"
    #
    # print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print("The content of the data is: {}\n".format(a_great_sentence))
    #
    # encoded_data, tree = huffman_encoding(a_great_sentence)
    #
    # print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print("The content of the encoded data is: {}\n".format(encoded_data))
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test 1:
    test_1_string = "There was a problem doing a push".lower()
    test_1_encoded, test_1_tree = huffman_encoding(test_1_string)
    test_1_decoded = huffman_decoding(test_1_encoded, test_1_tree)
    assert test_1_string == test_1_decoded

    # Test 2:
    test_2_string = "the quick brown fox jumps over the lazy dog".lower()
    test_2_encoded, test_2_tree = huffman_encoding(test_2_string)
    test_2_decoded = huffman_decoding(test_2_encoded, test_2_tree)
    assert test_2_string == test_2_decoded

    # Test 3:
    test_3_string = "it's time to eat".lower()
    test_3_encoded, test_3_tree = huffman_encoding(test_3_string)
    test_3_decoded = huffman_decoding(test_3_encoded, test_3_tree)
    assert test_3_string == test_3_decoded

    # Test 4:
    test_4_string = ""
    test_4_encoded, test_4_tree = huffman_encoding(test_4_string)
    test_4_decoded = huffman_decoding(test_4_encoded, test_4_tree)
    assert test_4_string == test_4_decoded

    tes_5_string = 12
    test_5_encoded, tes_5_tree = huffman_encoding(tes_5_string)


    print("All test passed....!!")
