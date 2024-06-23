from typing import *

# https://leetcode.com/problems/valid-anagram/description/

''' Notes

'''

''' Complexities 

Solution #1
Time Complexity: O(n)
Space Complexity: O(n)
- Use a hashmap and loops to keep track of the differences of char occurrences between the s and t strings
- Check to see if there's any difference in values after the loops, thus revealing wether or not the two strs are anagrams
'''

class Solution:
    # Solution 1
    def isAnagram(self, s: str, t: str) -> bool:
        s_t_char_occurrences_diff = {}

        # add the char occurrences of the s string
        for curr_char in s:
            if curr_char in s_t_char_occurrences_diff:
                s_t_char_occurrences_diff[curr_char] += 1
            else:
                s_t_char_occurrences_diff[curr_char] = 1
        
        for curr_char in t:
            if curr_char in s_t_char_occurrences_diff:
                s_t_char_occurrences_diff[curr_char] -= 1
            else:
                # we can return false here since we found a char that exists in t, but not in s
                return False
        
        for curr_val in s_t_char_occurrences_diff.values():
            if curr_val != 0:
                # we can return false here since there's a char occurrence difference between the two strings
                return False
        
        # default return
        return True
            
def main():
    solution = Solution()

    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t)) # true

    s = "rat"
    t = "car"
    print(solution.isAnagram(s, t)) # true

if __name__ == "__main__":
    main()
