class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        end_index_list = []
        
        for ind_elem, elem in enumerate(nums):
            second = target - elem
            if second in nums and ind_elem != nums.index(second):
                end_index_list = [nums.index(second), ind_elem]
                break
        

            
        end_index_list.sort()
        return end_index_list


# SEE result
print(Solution().twoSum([0, 4, 6, 0], 0))