###   7. Reverse Integer ###
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_string = str(abs(x))
        num_digits = len(x_string)
        result = 0
        for index, chx in enumerate(x_string):
        	result = result + int(chx) * pow(10, index)
        if x < 0:
        	result = -result
        return result
    