class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={} #num->freq
        #create the hasmap of list nums with freq
        for num in nums:
            if num not in count:
                count[num]=0
            count[num]+=1
        
        #sort keys in descending and choose top k numbers
        sorted_keys=sorted(count,key=count.get,reverse=True)

        return sorted_keys[:k]