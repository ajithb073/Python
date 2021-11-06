# 6/11/2021

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = l1.val + l2.val
        carry = sum//10
        out = ListNode(sum%10)
        start = out
        while(l1.next and l2.next):
            l1 = l1.next``
            l2 = l2.next
            sum = l1.val + l2.val + carry
            carry = sum//10``
            out.next = ListNode(sum%10)
            out = out.next
        while(l1.next):
            l1 = l1.next
            sum = l1.val + carry
            carry = sum//10
            out.next = ListNode(sum%10)
            out = out.next
        while(l2.next):
            l2 = l2.next
            sum = l2.val + carry
            carry = sum//10
            out.next = ListNode(sum%10)
            out = out.next
        if(carry>0):
            out.next = ListNode(carry)
        return start
    
