import math


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        count = dividend / divisor
        if count > 0:
            result = math.floor(count)
        else:
            result = math.ceil(count)
        max_count = pow(2, 31) - 1
        if result > max_count:
            return max_count
        else:
            return result


if __name__ == '__main__':
    solu = Solution()
    print(solu.divide(-2147483648, -1))
