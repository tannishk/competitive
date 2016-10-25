class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def node_count(node):
    assert hasattr(node, 'next'), node
    c = 1
    first = id(node)
    while node.next is not None:
        node = node.next
        if id(node) == first:
            # detected loop
            break
        c += 1
    return c

def test():
    first = Node(0)
    print(node_count(first))
    node = Node(1)
    first.next = node
    print(node_count(first))
    for i in range(3):
        node.next = Node(i+2)
        node = node.next
        print(node_count(first))
    # detects loops
    node.next = first
    print(node_count(first))

if __name__ == '__main__':
    test()
