# Apply cycle sort for this problem -> allowing the solution to run in O(n) time without using any extra space. 
# Other solutions, like using set, will also work for this, but not optimal in space complexity

class Solution:
  def findDuplicates(self, nums: List[int]) -> List[int]:
        idx = 0 
        while idx < len(nums):
            correct = nums[idx] - 1 
            if nums[correct] != nums[idx]:
                nums[idx], nums[correct] = nums[correct], nums[idx]
            else:
                idx += 1 
        
        result = []

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                result.append(nums[i])
        
        return result
        
