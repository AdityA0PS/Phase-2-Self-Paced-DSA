class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sorted(nums) == nums[::-1]:
            nums.sort()
        else:
            for i in reversed(range(1, len(nums))):
                if nums[i - 1] < nums[i]:
                    to_be_replaced = nums[i - 1]
                    nums_lst = sorted(nums[i - 1:len(nums)])
                    u_lst = sorted(list(set(nums_lst)))
                    next_bigger_num = u_lst[u_lst.index(to_be_replaced) + 1]
                    nums_lst.remove(next_bigger_num)
                    nums[i - 1:len(nums)] = [next_bigger_num, *nums_lst]
                    break
        