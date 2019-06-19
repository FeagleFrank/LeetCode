# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        len_list = 0
        it = head
        l = []
        while 1:
            len_list += 1
            l.append(it)
            if not it.next:
                break

            it = it.next
        if len_list == n:
            if n == 1:
                return []
            else:
                return head.next
        l[len_list-n-1].next = l[len_list-n].next
        return head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    it = head
    for i in [2, 3, 4, 5]:
        it.next = ListNode(i)
        it = it.next

    nit = s.removeNthFromEnd(head, 2)
    while 1:
        print(nit.val)
        if not nit.next:
            break
        nit = nit.next


# [1] 1
# [1, 2] 1
# [1, 2] 2

# Runtime: 44ms
