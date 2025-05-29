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
    
    
    
    def isPalindrome_complex(self, x):
        return str(x) == ''.join(reversed(str(x)))
    
    
    
    def isPalindrome_simple(self, x):
        return str(x) == str(x)[::-1]
    
    
    
    def isPalindrome_4(self, x):
        if x<0 or (x%10==0 and x!=0):
            return False

        k = 0
        string_num = str(x)
        while True:
            try:
                if string_num[k] != str(x%10):
                    return False
                x = x//10
                k+=1
            except:
                return True
            
            
            
    def isPalindrome_numerical(self, x):
        if x<0 or (x%10==0 and x!=0):
            return False

        original = x
        reverse = 0
        while x>0:
            reverse = reverse*10 + x%10
            x= x//10
        return original == reverse
