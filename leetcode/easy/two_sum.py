class Solution:
    def __init__(self):
        self.indices = []

    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, val in enumerate(nums):
            if (target - val) in nums[index + 1:]:
                self.indices = [index, nums.index(target - val, index + 1)]
                break
        return self.indices

    def nice_two_sum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                self.indices = [buff_dict[nums[i]], i]
                break
            else:
                buff_dict[target - nums[i]] = i
        return self.indices


if __name__ == '__main__':
    solu = Solution()
    print(solu.two_sum([3, 6, 3], 6))
    print(solu.nice_two_sum([3, 6, 3], 6))
