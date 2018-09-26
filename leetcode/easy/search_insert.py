class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = int((low + high) / 2)
            guess = nums[mid]
            if guess == target:
                index = mid
                break

            if guess > target:
                high = mid - 1

            else:
                low = mid + 1

        else:
            index = low

        return index


if __name__ == '__main__':
    solu = Solution()
    print(solu.searchInsert([1, 3, 5, 6], 0))
    # print(solu.searchInsert([1, 3, 4, 5, 7], 2))
