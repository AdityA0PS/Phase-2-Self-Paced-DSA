class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        arr = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l = j+1
                r = len(nums)-1
                while l < r:
                    if nums[l] + nums[r] + nums[i] + nums[j] ==target :
                        a = [nums[i],nums[j],nums[l],nums[r]]
                        if a not in arr:
                            arr.append(a)
                            l+=1
                        else:
                            l+=1
                    elif nums[l] + nums[r] + nums[i] + nums[j] > target:
                        r-=1
                    else:
                        l+=1    
        return arr
        