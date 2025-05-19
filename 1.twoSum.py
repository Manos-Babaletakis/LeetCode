from dotenv import load_dotenv, dotenv_values 
import os
# loading variables from .env file
load_dotenv()
local_path = os.getenv("LOCAL_PATH")

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, num in enumerate(nums):
            dic[target - num] = index
        for index, num in enumerate(nums):
            if num in dic:
                if dic[num] != index:
                    if dic[num] > index:
                        return [index, dic[num]]
                    return [dic[num], index]
                
        

numbers = [3,6,7,2,12,15,22]
target = 29

sol = Solution()
print(sol.twoSum(numbers, target))