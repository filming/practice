from typing import *

# https://leetcode.com/problems/contains-duplicate/description/

''' Notes

'''

''' Complexities 

Solution #1
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    # Solution 1
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_nums = set()

        for curr_num in nums:
            if curr_num in seen_nums:
                return True
            
            seen_nums.add(curr_num)
        
        return False

def main():
    solution = Solution()

    nums = [1,2,3,1]
    print(solution.containsDuplicate(nums)) # true

    nums = [1,2,3,4]
    print(solution.containsDuplicate(nums)) # false

    nums = [1,1,1,3,3,4,3,2,4,2]
    print(solution.containsDuplicate(nums)) # true

if __name__ == "__main__":
    main()
