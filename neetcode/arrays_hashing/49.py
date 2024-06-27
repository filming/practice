from typing import *

# https://leetcode.com/problems/group-anagrams/description/

''' Solutions 

[ Solution #1 ]

Time Complexity:
- O(k(n log n))
- k is the length of the total amount of strings in strs
- n is the length of a string in strs
- Iterating over each string in strs has a TC of O(n) 
- Sorting a string using TimSort has a TC of O(n log n)

Space Complexity:
- O(n)
- In the worst case, when sorting and comparing, we can find no common sorted anagrams which means our grouped_anagrams hashmap will have the same number of elements as the given strs list.
- We will need to create a new string after each iteration of our loop, which will be a O(n) operation.

Approach:
- Create a hashmap that will store our grouped anagrams (call it grouped_anagrams). A string containing the sorted characters of an anagram will be the key and the associated value being a list containing strings that if sorted, would yield the same string as the key. Initialize this hashmap as empty.
- Create a loop that will iterate through each string in the given strs list, starting from the first string and stopping after the last one.
- For each string in the loop, sort the string using TimSort algorithm. 
- Check and see if this newly sorted string is in grouped_anagrams as a key. If it is, add the pre-sorted string to the list which is stored as the key's associated value. If it is not, add the newly sorted string as a key in grouped_anagrams with the associated value being a list containing the pre-sorted string / currently iterated string in strs.
- The return value will be a list of all the values stored in grouped_anagrams.

Notes:
- TimSort algorithm (or sorted() in Python) has a time complexity of O(n log n).

'''

class Solution:
    # Solution 1
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}

        for curr_str in strs:
            curr_str_sorted = "".join(sorted(curr_str))
            
            if curr_str_sorted in grouped_anagrams:
                grouped_anagrams[curr_str_sorted].append(curr_str)
            else:
                grouped_anagrams[curr_str_sorted] = [curr_str]
                
        return grouped_anagrams.values()

def main():
    solution = Solution()

    strs = ["eat","tea","tan","ate","nat","bat"]
    print(solution.groupAnagrams(strs)) # [["bat"],["nat","tan"],["ate","eat","tea"]]

    strs = [""]
    print(solution.groupAnagrams(strs)) # [[""]]

    strs = ["a"]
    print(solution.groupAnagrams(strs)) # [["a"]]

if __name__ == "__main__":
    main()
