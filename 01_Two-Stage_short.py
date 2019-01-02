class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # nums_indexed = {}  # record  nums-indexes to nums-values
        end_index_list = []  # record nums_indexed-keys final pass

        # for i in range(len(nums)):
        #     if i <= target:
        #         nums_indexed[i] = nums[i]

        # for elem in nums_indexed.items():
        #     for sec_elem in nums_indexed.items():
        #         if target - elem[1] == sec_elem[1] and elem[0] < sec_elem[0]:
        #             end_index_list = [elem[0], sec_elem[0]]

        for elem in range(len(nums)):
            if target - nums[elem] in nums and elem < nums.index(target - nums[elem]):
                end_index_list = [elem, nums.index(target - nums[elem])]
                print(end_index_list)

        return end_index_list


# SEE result
print(Solution().twoSum([0, 4, 6, 0], 0))