class Node(object):
    """
    class used to represent a Node.
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __iter__(self):
        nodes = [self]
        while nodes[-1].has_next():
            nodes.append(nodes[-1].next_node)
        return iter(nodes)

    def has_next(self):
        return self.next_node is not None


def get_linked_list_length(n):
    """
    Get length of list given a starting node.
    :param n: Node that may or may not have following Nodes
    :type n: Node
    :return: The length of the list starting at the given Node
    :rtype: int
    """
    return len([_ for _ in iter(n)])


def main():
    nodes = Node(data=1, next_node=Node(data=2, next_node=Node(data=3)))
    length = get_linked_list_length(nodes)
    print(length)


if __name__ == '__main__':
    main()
