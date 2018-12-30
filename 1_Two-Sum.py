class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_indexed = {}  # record  nums-indexes to nums-values
        result_list = []  # record nums_indexed-keys final pass
        sum_list = []

        for item in nums:
            nums_indexed[nums.index(item)] = item

        for key_first, value_first in nums_indexed.items():

            result_list.append(key_first)
            sum_list.append(nums_indexed[key_first])


            for elem in nums_indexed.keys():

                result_list.append(elem)
                sum_list.append(nums_indexed[elem])

                if len(sum_list) == 2 and sum(sum_list) == target:
                    break
                else:
                    result_list.pop()
                    sum_list.pop()

            if len(result_list) == 2 and result_list[0] == result_list[1]:
                del result_list[:0]
                del sum_list[:0]
            else:
                pass

            if sum(sum_list) == target:
                break
            else:
                result_list.pop()
                sum_list.pop()

        return result_list


print(Solution().twoSum([2, 6, 6, 15], 8))