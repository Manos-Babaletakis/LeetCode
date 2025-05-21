import os

from dotenv import load_dotenv, dotenv_values 
load_dotenv()
local_path = os.getenv("LOCAL_PATH")

class Solution(object):
    def bigger_list(self, list_1, list_2):
        if len(list_1) > len(list_2):
            return list_2, list_1
        return list_1, list_2
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """    
        #make sure len(nums1) >= len(nums2)     
        nums1, nums2 = self.bigger_list(nums1, nums2)
        
        m_max = len(nums1) #total items of nums1
        n_max = len(nums2) #total items of nums2
        
        total = m_max + n_max #total items of nums1 + nums2 (total list)
        left = (m_max + n_max + 1) // 2 #total items of left partition of total list
        low = 0 #first item of total list
        high = m_max #last item of nums1(biggest sublist)
        
        while low <= high:
            mid_m = (low + high) // 2 # find the mid index for nums1
            mid_n = left - mid_m # find the mid index for nums2
            
            l_m = float('-inf')
            l_n = float('-inf')
            r_m = float('inf')
            r_n = float('inf')
            
            if mid_m < m_max:
                r_m = nums1[mid_m]
            if mid_n < n_max:
                r_n = nums2[mid_n]
            if mid_m - 1 >= 0:
                l_m = nums1[mid_m - 1]
            if mid_n - 1 >= 0:
                l_n = nums2[mid_n - 1]
            
            if l_m <= r_n and l_n <= r_m:
                if total % 2 == 1:
                    return max(l_m, l_n)
                else:
                    return (max(l_m, l_n) + min(r_m, r_n)) / 2.0
            elif l_m > r_n:
                high = mid_m - 1
            else:
                low = mid_m + 1
        
        return 0
        
            
list_1 = [1, 10, 35]
list_2 = [1, 2, 5, 8, 14, 35.5, 78, 79, 80, 80.5, 81, 99, 101]
output=35.25

sol = Solution()
print(sol.findMedianSortedArrays(list_1, list_2) == output)