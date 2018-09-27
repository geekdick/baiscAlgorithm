class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        result = True
        for i in range(int(len(x) / 2)):
            if x[i] != x[-i - 1]:
                result = False
                break
        return result