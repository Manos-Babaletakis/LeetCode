class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        length = len(str(x))
        half = length//2
        k=0
        while k<=half:
            if str(x)[k] != str(x)[length - 1 - k]:
                return False
            k+=1
        return True