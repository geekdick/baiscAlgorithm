# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    _head = None

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 1:
            return head
        new_head = self.get_new_head(head)
        new_tail = head
        for i in range(0, k):
            new_head=new_head.next

    def get_new_head(self, head):
        old_head = head
        new_head = head
        while 1:
            next_node = new_head.next

            if not next_node:
                break
            else:
                new_head = next_node
        new_head.next = old_head

        return new_head

    def gen_node_list(self, node_val_list):
        node_list = [ListNode(val) for val in node_val_list]
        head = node_list[0]
        for index in range(len(node_list) - 1):
            node_list[index].next = node_list[index + 1]

        return head

    def loop_node_list(self, link):
        while True:

            print(link.val)
            link = link.next

            if not link:
                break


if __name__ == '__main__':
    solu = Solution()
    links = solu.gen_node_list([1, 2, 3, 4, 5])
    links = solu.rotateRight(links, 2)
    # solu.loop_node_list(links)
