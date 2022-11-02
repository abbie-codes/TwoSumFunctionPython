"""
Two Sum
------------------------------------------------------------------------------------------------------------------------
Given an array of integers nums and an integer target, return two numbers inside that array such that they add up to a
target.

You may assume that each input would have at least one solution, and you may not use the same element twice.

You can return the answer in any order.

EXAMPLE 1:
---------------------------------------------------------------
Input: nums = [2,7,11,15], target = 9
Output: [2, 7]
Explanation: Because nums[0] + nums[1] == 9, we return [2, 7].

EXAMPLE 2:
---------------------------------------------------------------
Input: nums = [3,2,4], target = 6
Output: [2, 4]

EXAMPLE 3:
---------------------------------------------------------------
Input: nums = [3,3], target = 6
Output: [3, 3]

NOTES:
---------------------------------------------------------------
- An input MAY HAVE no two numbers at all (an empty one still counts as a solution) - in this case, return a empty array
- It's an array of integer numbers - these numbers are not necessarily distinct / unique
- Make sure to discuss your solution - what is the Big O Time & Space complexity? Was there anyway you could've done...
...better or not? Why or why not? Justify.
"""

nums = [2, 7, 11, 15]
target = 9

def twoSum(array, total):

    size = len(array)

    if size == 0:
        print(f"Explanation: because the array is empty, we return {solution}.")

    solution = []

    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if (array[i] + array[j] == total):
                solution.append(array[i])
                solution.append(array[j])
                print(f"Explanation: because {array[i]} plus {array[j]} equals {total}, we return {solution}.")

twoSum(nums, target)

"""
-----------------------------------------------------------------------------------------------------------------------
Solution Explanation: 

    if size == 0:
        print(f"Explanation: because the array is empty, we return {solution}.")

This part of the solution makes sure that an empty array is returned if their are no numbers in the array.
Size is calculated above by using the in built function len() and taking in the array argument to calculate the size. 
The solution is then printed out in a way which is easy to understand. 

    for i in range(0, size - 1):

This part of the function iterates through every element in the array.

    for j in range(i + 1, size):

Within that iteration this part of the function iterates through the next element in the array.

    if (array[i] + array[j] == total):

Within that iteration, this part of the function checks if the 2 numbers sum up to the total number (passed as an 
argument). 

An empty array called 'solution' is declared before this part of the function, if the 'if statement' above is true, the 
two numbers are appended to the empty solution array. The solution is then printed out in a way which is easy to 
understand.

I think that the Big O Time & Space complexity is Quadratic O(N2) because of the nested for loop on line 48,
the remainder of the function would be Constant O(1) which would likely be dismissed, because the first part checks if length 
of the array is 0, so the time to check this will always be the same, and the last part of the function will always add 2 numbers. 
But for the nested loop, if the data set was extremely large then the time to loop through all of the numbers and adjacent numbers 
would be increased considerably, this could be improved by making sure that the size of the array is always the same (Constant O(1)) 
and by only using one loop through the array (Linear O(N)), however I am not sure how you could achieve the same solution by 
only using one loop. 
--------------------------------------------------------------------------------------------------------------------------
"""
