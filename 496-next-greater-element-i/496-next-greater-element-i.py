class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        ht = {val: i for i, val in enumerate(nums1)}
        st = [] # stack

        for n in reversed(nums2):
            while st and st[-1] < n:
                st.pop()

            if st and (n in ht):
                res[ht[n]] = st[-1]

            st.append(n)

        return res
        