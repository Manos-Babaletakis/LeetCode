import os

from dotenv import load_dotenv, dotenv_values 
load_dotenv()
local_path = os.getenv("LOCAL_PATH")

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {} #dic[letter] = [last_index, max_dis]
        k = 0
        max = 0
        last_double = 0
        for index, letter in enumerate(s):
            k+=1
            if letter in dic:
                if dic[letter] > index- k:
                    k= index - dic[letter]
                    
            dic[letter] = index
            if max < k:
                max = k
        
        return max
    
total_string = 'dvtdtxurd'
output = 5

sol = Solution()
print(sol.lengthOfLongestSubstring(total_string) == output)