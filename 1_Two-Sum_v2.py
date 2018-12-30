class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_indexed = {}  # record  nums-indexes to nums-values
        end_index_list = []  # record nums_indexed-keys final pass
        sum_list = []

        for item in nums:
            nums_indexed[nums.index(item)] = item

        for nums_item in nums_indexed.items():

            end_index_list.append(nums_item[0])
            sum_list.append(nums_item[1])

            for elem in nums_indexed.items():

                end_index_list.append(elem[0])
                sum_list.append(elem[1])

                if len(sum_list) == 2 and sum(sum_list) == target:

                    if end_index_list[1] - end_index_list[0] == 1:
                        break
                    else:
                        pass
                        # del end_index_list[0]
                        # del sum_list[0]
                        # continue
                else:
                    end_index_list.pop()
                    sum_list.pop()


            if sum(sum_list) == target:

                if end_index_list[1] - end_index_list[0] == 1:
                    break
                else:
                    del end_index_list[0]
                    del sum_list[0]
                    # continue
            # else:
            #     end_index_list.pop()
            #     sum_list.pop()

        return end_index_list


# SEE result
print(Solution().twoSum([2, 6, 6, 15], 8))
