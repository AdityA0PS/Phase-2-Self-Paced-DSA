class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        li=[]
        i=0
        j=0
        
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                li.append(nums1[i])
                i+=1
            else:
                li.append(nums2[j])
                j+=1
        while i<m:
            li.append(nums1[i])
            i+=1
        while j<n:
            li.append(nums2[j])
            j+=1
         
        print(li)
        l = len(li)
        
        if l%2==0:
            i = l/2
            j = l/2 - 1
            res = (li[int(i)] + li[int(j)])/2
            res = float(res)
            return res
        else:
            i = (l-1)/2
            res = li[int(i)]
            res = float(res)
            return res
            
                
          
        