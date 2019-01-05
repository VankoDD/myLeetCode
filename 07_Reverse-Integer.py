class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        lim32 = 2 ** 31

        end_result = int("".join(str(abs(x))[::-1]).strip())

        if x < 0:
            end_result = end_result*-1

        if not(end_result in range(-lim32, lim32)) or end_result == 0:
            end_result = 0

        return end_result


print(Solution().reverse(15342))