class Solution:
    def mergeTwoLists(self, list1, list2):
        itr = list1
        nodes1 = []
        if itr:
            while itr.next: 
                nodes1.append(itr)
                itr = itr.next
            nodes1.append(itr)
        itr = list2
        nodes2 = []
        if itr:
            while itr.next: 
                nodes2.append(itr)
                itr = itr.next
            nodes2.append(itr)    
        n1 = len(nodes1)
        n2 = len(nodes2)
        if n1+n2 > 0:
            arr = [None] * (n1+n2)
            i = 0 
            j = 0
            k = 0
        
            while i < n1 and j < n2:
                if nodes1[i].val <= nodes2[j].val:
                    arr[k] = nodes1[i]
                    i += 1
                else:
                    arr[k] = nodes2[j]
                    j += 1
                k += 1

            while i < n1:
                arr[k] = nodes1[i]
                i += 1
                k += 1
        
            while j < n2:
                arr[k] = nodes2[j]
                j += 1
                k += 1
            i = 0
            while i < (n1+n2) - 1:
                arr[i].next = arr[i+1]
                i += 1
            return arr[0] 
        else:
            return list1