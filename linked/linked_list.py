from linked import Node


class LinkedList:
    def __init__(self):
        self._size = 0
        self._head = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def extends(self, seqs):
        pass

    def add_node(self, index, element):
        """ 在链表index位置添加元素"""
        if index == 0:
            self.add_first(element)
        else:
            pre_node = self.find_node(index - 1)
            cur_node = pre_node.next_node
            pre_node.next_node = Node(element, cur_node)
            self._size += 1

    def find_node(self, index):
        """ 查找索引为index的node"""
        assert 0 <= index <= self._size
        node = self._head
        for i in range(index):
            node = node.next_node
            if not node:
                break

        return node

    def add_first(self, element):
        """ 在链表头添加元素"""
        self._head = Node(element=element, next_node=self._head)
        self._size += 1

    def append(self, element):
        """ 在链表头尾加元素"""
        index = self._size
        self.add_node(index, element)

    def __str__(self):
        return str(self._head)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(555)
    ll.append(3)
    ll.append(5)
    ll.append(7)
    ll.append(9)
    ll.append(66)
    ll.append(44)
    ll.append(33)
    print(ll)
