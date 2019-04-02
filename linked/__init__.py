class Node:
    __slots__ = 'element', 'next_node'

    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node

    def __str__(self):
        return '{} ->{}'.format(self.element, self.next_node)

    def __repr__(self):
        return self.__str__()
