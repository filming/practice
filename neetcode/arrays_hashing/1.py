from typing import *

# https://leetcode.com/problems/two-sum/description/

''' Solutions 

Solution #1
Time Complexity:
- O(n^2)
Space Complexity:
- O(1)
Approach:
- Create a for-loop (i) that will iterate from the 0th index pos and end at the last index pos of nums
- Create a nested for-loop (j) inside of loop-i that will iterate starting from the 0th index pos and end at the last index pos of nums 
- Create a variable to keep track of the desired complementary number
- Complementary number is equal to the current value of nums[i] subtracted from the target value.
- This complementary number should be updated after each iteration of loop-i
- Check and see if the current value of nums[j] is equal to this complementary number and also make sure that i ≠ j, returning an array of [i,j] if so
- i ≠ j because that means they would be pointing to the same index and value in nums. Can't have a pairing with the same entity twice.
- The default return can be an array containing negative numbers to indicate no valid indices could be found
Notes:
- 

Solution #2:
Time Complexity:
- O(n)
Space Complexity: 
- O(n)
Approach:
- Create a hashmap (call it nums_indices), this will store an int from nums as a key and its index as the a value. Initialize it empty.
- Create a for-loop (call it loop-i) that will iterate from the 0th index pos and end at the last index pos of nums.
- Create a variable to keep track of the desired complementary number
- Complementary number is equal to the current value of nums[i] subtracted from the target value.
- Complementary number should be updated at the top of loop-i
- Check to see if the current value of the complementary number is in nums_indices. If it is then return an array pairing of the value associated with the key and the current index value of i. If it is not then add nums[i] to nums_indices with the associated value being i.
- The default return can be an array paring containing negative numbers to indicate no valid indices could be found.
Notes:
- A hashmap will allow quicker lookup times than a list. O(1) compared to O(n) if we're just checking to see if an element exists in it or not.

'''

class Solution:
    # Solution 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (0, len(nums)):
            complementary_num = target - nums[i]

            for j in range (0, len(nums)):
                if (complementary_num == nums[j]) and (i != j):
                    return [i, j]
        
        return [-1, -1]
    
    # Solution 2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indices = {}

        for i in range (0, len(nums)):
            complementary_num = target - nums[i]

            if complementary_num in nums_indices:
                return [nums_indices[complementary_num], i]
            
            else:
               nums_indices[nums[i]] = i

        return [-1, -1] 

def main():
    solution = Solution()

    nums = [2,7,11,15]
    target = 9
    print(solution.twoSum(nums, target)) # [0,1]

    nums = [3,2,4]
    target = 6
    print(solution.twoSum(nums, target)) # [1,2]

    nums = [3,3]
    target = 6
    print(solution.twoSum(nums, target)) # [0,1]

    nums = [2,5,5,11]
    target = 10
    print(solution.twoSum(nums, target)) # [1,2]

if __name__ == "__main__":
    main()
