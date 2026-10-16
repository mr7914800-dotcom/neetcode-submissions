class Solution:
    def hasDuplicate(self, numList: List[int]) -> bool:
        d=dict()
        """for k in nums:
            if k in d.keys():
                d[k]+=1
                if d[k]>1:
                    return True
            else:
                d[k]=1
        return False"""

        
        for k in numList:
            d[k]=d.get(k,0)+1#check key exists
            if d[k] >1:
                return True
        return False            

       # if len(nums)==len(set(nums)):
        #    return False
       # else:
        #    return True
        
        
        