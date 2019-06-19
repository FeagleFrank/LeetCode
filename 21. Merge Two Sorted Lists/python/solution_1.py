# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.val) + ' -> ' + str(self.next)
        return str(self.val)


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def insert(pre, n1, n2):
            # if not pre:
            if not n1 and not n2:
                return
            elif not n1 or n2 and n1.val > n2.val:
                pre.next = n2
                insert(pre.next, n1, n2.next)
            else:
                pre.next = n1
                insert(pre.next, n1.next, n2)

        pre = ListNode(0)
        insert(pre, l1, l2)
        return pre.next


if __name__ == '__main__':
    # s = Solution()
    # l1 = ListNode(1)
    # l1.next = ListNode(2)
    # l1.next.next = ListNode(4)
    # l2 = ListNode(1)
    # l2.next = ListNode(3)
    # l2.next.next = ListNode(4)
    # # it = head
    # # for i in [2, 3, 4, 5]:
    # #     it.next = ListNode(i)
    # #     it = it.next
    # # s = Solution()
    # print(s.mergeTwoLists(l1, l2))

    s = Solution()
    l1 = ListNode(1)
    l2 = None
    print(s.mergeTwoLists(l2, l1))


# Runtime: 56 ms
