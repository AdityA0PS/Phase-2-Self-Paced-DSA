class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries=sorted( [q[1],q[0],i] for i,q in enumerate(queries))
        trie={}
        def insert2trie(a):
            nd=trie
            for i in range(31,-1,-1):
                bit=(a>>i)&1
                if bit not in nd:
                    nd[bit]={}
                nd=nd[bit]
        def queryTrie(b):
            ## maximize b with numbers in trie
            res=0
            nd=trie
            for i in range(31,-1,-1):
                if not nd:
                    return -1
                bit=(b>>i)&1
                if 1-bit in nd:
                    nd=nd[1-bit]
                    res|=(1<<i)
                else:
                    nd=nd[bit]
            return res
        n=len(queries)
        res=[-1]*n
        i=0
        for j, q in enumerate(queries):
            while i<len(nums) and nums[i]<=q[0]:
                insert2trie(nums[i])
                i+=1
            res[q[2]]=queryTrie(q[1])
        return res
        