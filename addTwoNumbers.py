class Solution:
    def addTwoNumbers(self, l1, l2):
        round = 0
        head = ListNode(0)
        currentNode = head
        while l1 or l2:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            val = (val1 + val2 + round)%10
            round = int((val1 + val2 + round)/10)  if val1 + val2 + round > 9 else 0
            currentNode.next = ListNode(val)
            currentNode = currentNode.next
        if round == 1: currentNode.next = ListNode(round)
        return head.next
