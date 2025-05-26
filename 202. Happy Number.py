#find if the number's digit's squares equal to one after addition or if their sum's digits do. If there is a loop return false
class Solution(object):
    def __init__(self):
        self.number_list = []
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        if n in self.number_list:
            return False
        self.number_list.append(n)
        for number in str(n):
            sum += int(number)**2
        if sum == 1:
            return True
        return self.isHappy(sum)