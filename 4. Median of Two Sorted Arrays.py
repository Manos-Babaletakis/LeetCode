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
        
        placeholder_1 = 0
        placeholder_2 = 0
        
        m=0
        n=0
        
        for _ in range(0, (m_max + n_max)//2 + 1):
            placeholder_2 = placeholder_1
            if m < m_max and n < n_max:
                if nums1[m] < nums2[n]:
                    placeholder_1 = nums1[m]
                    m += 1
                else:
                    placeholder_1 = nums2[n]
                    n += 1
            elif m < m_max:
                placeholder_1 = nums1[m]
                m += 1
            else:
                placeholder_1 = nums2[n]
                n += 1
        
        if (m_max + n_max)%2 == 1:
            return placeholder_1
        else:
            return (placeholder_1 + placeholder_2)/2
            
list_1 = [1, 10, 35]
list_2 = [1, 2, 5, 8, 14, 35.5, 78, 79, 80, 80.5, 81, 99, 101]
output=35.25

sol = Solution()
print(sol.findMedianSortedArrays(list_1, list_2) == output)