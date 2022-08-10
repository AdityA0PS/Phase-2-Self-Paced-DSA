class Solution:
    def singleNonDuplicate(self, nums):
        low, high = 0, len(nums)-1
    
        while low <= high:
            mid = (low + high)//2
        
            if mid%2 == 1:
                if mid-1 >= 0 and nums[mid] == nums[mid-1]:
                    low = mid + 1
                elif mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                    high = mid - 1
                else:
                    return nums[mid]
            else:
                if mid-1 >= 0 and nums[mid] == nums[mid-1]:
                    high = mid - 2
                elif mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                    low = mid + 2
                else:
                    return nums[mid]
            
        return nums[low]
        