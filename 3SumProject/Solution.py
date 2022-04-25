'''
Created on Apr 22, 2022

@author: David J. Roche
'''

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

#Approach: Two-Pointer
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #return empty list if nums list has less than 3 value
        if len(nums) < 3:
            return []
        if (all(num == 0 for num in nums)):
            return [[0,0,0]]
        size = len(nums)
        num_found = {}
        nums = sorted(nums)
        for i, val in enumerate(nums):
            left = i + 1          # starting pointer points to next
            right = size - 1      #end pointer points to last element in nums
            
            while left < right:
                total = val + nums[left] + nums[right]
                if total == 0:   #find the total (sum) that equals to zero (0)
                    actual = (val, nums[left], nums[right])
                    
                    if actual not in num_found:
                        num_found[actual] = True
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return list(num_found.keys())
    


'''
Complexity analysis as follow:
Time Complexity: O(n^2)
Space Complexity: O(n)
I used one for-loop to yield the values of x, and for each value of x, it pairs up with
y and z such that x+y+z=0 using the two-pointer method that, itself, takes O(n) time. Therefore, O(n^2) 
is the time complexity.
'''