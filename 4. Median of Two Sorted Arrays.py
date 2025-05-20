import os

from dotenv import load_dotenv, dotenv_values 
load_dotenv()
local_path = os.getenv("LOCAL_PATH")

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m_max = len(nums1)
        n_max = len(nums2)
        
        m = m_max//2 + m_max%2
        n = n_max//2 + n_max%2
        
        if (m_max+n_max)%2 == 1:
            
            
list_1 = [1, 10, 35]
list_2 = [1, 2, 5, 8, 14, 35, 78, 79, 80, 80.5, 81, 99, 101]

sol = Solution()
print(sol.lengthOfLongestSubstring(total_string) == output)