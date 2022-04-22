# -3Sum from Leetcode
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Point of view:
I have some experience coding in python, but I have to admit finding and accepted result for this program
was a bit challenging because, for a moment, I failed/forgot to sort the list before iterating thru it.

Here is my approach & analysis:
I used one for-loop to yield the values of x, and for each value of x, it pairs up with
y and z such that x+y+z=0 or y+z=x using the two-pointer method that, itself, takes O(n) time. Therefore, O(n^2) 
is the time complexity.
