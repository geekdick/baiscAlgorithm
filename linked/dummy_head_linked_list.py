from linked import Node


class LinkedList:
    def __init__(self):
        self._size = 0
        self._dummy_head = Node()

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def extends(self, seqs):
        pass

    def add_node(self, index, element):
        """ 在链表index位置添加元素"""

        pre_node = self.find_node(index - 1)
        cur_node = pre_node.next_node
        pre_node.next_node = Node(element, cur_node)
        self._size += 1

    def find_node(self, index):
        """ 查找索引为index的node"""
        assert -1 <= index <= self._size
        node = self._dummy_head
        for i in range(index + 1):
            node = node.next_node
            if not node:
                break

        return node

    def add_first(self, element):
        """ 在链表头添加元素"""
        self.add_node(0, element)

    def append(self, element):
        """ 在链表头尾加元素"""
        index = self._size
        self.add_node(index, element)

    def set_node(self, index, element):
        """ 修改链表index位置element值"""
        cur_node = self.find_node(index)
        cur_node.element = element

    def contains(self, element):
        """ 判断链表是否含有值为element节点"""
        node = self._dummy_head
        for i in range(self._size):
            node = node.next_node
            if node.element == element:
                return True
        return False

    def delete_node(self, index):
        """ 删除index节点元素"""
        node = self.find_node(index - 1)
        node.next_node = node.next_node.next_node

    def __str__(self):
        return str(self._dummy_head.next_node)

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
    ll.add_first(1243)
    ll.add_first(7889)
    print(ll)
    ll.set_node(4, 1243254345)
    print(ll)
    print(ll.contains(55))
    ll.delete_node(0)
    ll.delete_node(9)
    print(ll)
