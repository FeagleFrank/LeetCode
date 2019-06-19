# Definition for singly-linked list.
import copy
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        f = 0
        n1 = l1.val
        n2 = l2.val
        r = ListNode((n1 + n2) % 10 + f)
        re = r
        f1 = False
        f2 = False
        while 1:
            f = (n1 + n2 + f) // 10
            if l1.next is None:
                n1 = 0
                f1 = True
            else:
                l1 = l1.next
                n1 = l1.val
            if l2.next is None:
                n2 = 0
                f2 = True
            else:
                l2 = l2.next
                n2 = l2.val
            if f1 and f2 and f == 0:
                return re
            r.next = ListNode(((n1 + n2) % 10 + f) % 10)
            r = r.next

if __name__ == '__main__':
    # l1 = ListNode(2)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)
    l1 = ListNode(1)
    l2 = ListNode(9)
    l2.next = ListNode(9)

    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    print(result.val)
    print(result.next.val)
    print(result.next.next.val)

# Run Time: 189 ms
