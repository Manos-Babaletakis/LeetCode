from dotenv import load_dotenv, dotenv_values 
import os
import numpy as np
# loading variables from .env file
load_dotenv()
local_path = os.getenv("LOCAL_PATH")

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        placeholder = ListNode()
        l3 = placeholder
        residue = 0
        
        while l1.val or l2.val or residue:
            sum = residue
            
            #check l1
            if l1.val:
                sum += l1.val
                l1 = l1.next

            #check l2
            if l2.val:
                sum += l2.val
                l2 = l2.next
            
            placeholder.next = ListNode(sum%10)
            placeholder = placeholder.next
            residue = sum//10
             
             
        return l3.next
        

# l1 = ListNode([9,9,9,9,9,9,9])
# l2 = ListNode([9,9,9,9])
# output = ListNode([8,9,9,9,0,0,0,1])

# sol = Solution()
# print(sol.addTwoNumbers(l1, l2) == output)