import os

from dotenv import load_dotenv, dotenv_values 
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
        
        while l1 or l2 or residue:
            sum = residue
            
            #check l1
            if l1:
                sum += l1.val
                l1 = l1.next

            #check l2
            if l2:
                sum += l2.val
                l2 = l2.next
            
            placeholder.next = ListNode(sum%10)
            placeholder = placeholder.next
            residue = sum//10
             
        return l3.next
        
        
        
list_1 = [9,9,9,9]          
placeholder_1 = ListNode()
l1 = placeholder_1  
for i in list_1:
    placeholder_1.next = ListNode(i)
    placeholder_1 = placeholder_1.next
    
    
list_2 = [9,9,9,9,9,9,9]
placeholder_2 = ListNode()
l2 = placeholder_2
for i in list_2:
    placeholder_2.next = ListNode(i)
    placeholder_2 = placeholder_2.next

list_o = [8,9,9,9,0,0,0,1]
placeholder_o = ListNode()
output = placeholder_o
for i in list_o:
    placeholder_o.next = ListNode(i)
    placeholder_o = placeholder_o.next


sol = Solution()
print(sol.addTwoNumbers(l1.next, l2.next) == output.next)