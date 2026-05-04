class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1, l2):
            merged = []
            i, j = 0, 0
            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    merged.append(l1[i])
                    i += 1
                else:
                    merged.append(l2[j])
                    j += 1
            
            while i < len(l1):
                merged.append(l1[i])
                i += 1

            while j < len(l2):
                merged.append(l2[j])
                j += 1
            
            return merged
        
        def recurseCall(l):
            if len(l) == 0:
                return []
            elif len(l) == 1:
                return l
            
            mid = len(l) // 2
            l1 = recurseCall(l[:mid])
            l2 = recurseCall(l[mid:])

            merged = merge(l1, l2)
            return merged

        

        return recurseCall(nums)
                