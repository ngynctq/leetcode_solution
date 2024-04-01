#Applying prefix sum
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixSum = {0: -1}
        totalSum = 0
        length = 0

        for i, num in enumerate(nums):
            if num == 0:
                totalSum -= 1 
            else:
                totalSum += 1 
            
            if totalSum in prefixSum:
                length = max(length, i - prefixSum[totalSum])
            
            else:
                prefixSum[totalSum] = i
        
        return length 
        
