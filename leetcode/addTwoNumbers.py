# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        left = 0
        while l1 or l2 or left == 1:
            (l1, num1) = (l1.next, l1.val) if l1 else (None, 0)
            (l2, num2) = (l2.next, l2.val) if l2 else (None, 0)
            left, num = divmod(num1 + num2 + left, 10)
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next


if __name__ == "__main__":
    test = Solution()
    list1 = [2,4,8]
    curr1 = head1 = ListNode(0)
    for num in list1 :
        curr1.next = ListNode(num)
        curr1 = curr1.next
    l1 = head1.next

    list2 = [5,6,4]
    curr2 = head2 = ListNode(0)
    for num in list2 :
        curr2.next = ListNode(num)
        curr2 = curr2.next
    l2 = head2.next

    l3 = test.addTwoNumbers(l1, l2)
    while l3 :
        print(l3.val)
        l3 = l3.next
