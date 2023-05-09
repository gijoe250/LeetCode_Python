from typing import List

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        for index1 in range(len(nums)):
            print ('Current num :', nums[index1])
            for index2 in range(len(nums)):
                if(index1 != index2 and nums[index1] + nums[index2] == target):
                    answer.extend([index1, index2])
                    return answer
        return answer

numbers = [2,7,11,15]
target = 9

print(Solution().twoSum(numbers, target))
