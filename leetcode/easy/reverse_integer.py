class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        str_x = str(x)
        sign = ''
        if str_x[0] == '-':
            sign = '-'
            str_x = str_x[1:]

        clean_x = str_x.rstrip('0')[::-1]
        result = int(sign + clean_x or 0)
        if not self.check_boundary(result):
            result = 0
        return result

    @classmethod
    def check_boundary(cls, nums):
        boundary = pow(2, 31)
        if nums > -boundary and (nums < boundary - 1):
            return True


if __name__ == '__main__':
    solu = Solution()
    print(solu.reverse(1534236469))
