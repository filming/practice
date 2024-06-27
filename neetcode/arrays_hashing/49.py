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

[ Solution #2 ]

Time Complexity:
- O(n * k)
- n is the total amount of strings in strs
- k is the average length of a string in strs
- Iterating over each string in strs is O(n).
- Creating a char occurrence list of a string is O(n).
- Converting a list of ints to a tuple of ints is O(n).
- Looking up the existance and/or updating values in a dict is O(1).

Space Complexity:
- O(n * k)
- n is the total amount of strings in strs
- k is the average length of a string in strs
- Creating a char occurrence list of a string is O(n).
- Converting a list of ints to a tuple of ints is O(n).
- In the worst case, when comparing, we can find no common sorted anagrams which means our grouped_anagrams hashmap will have the same number of elements as the given strs list. O(n)

Approach:
- Create a hashmap that will store our grouped anagrams (call it grouped_anagrams). A string containing the sorted characters of an anagram will be the key and the associated value being a list containing strings that if sorted, would yield the same string as the key. Initialize this hashmap as empty.
- Create a loop that will iterate through each string in the given strs list, starting from the first string and stopping after the last one.
- For each string in the loop, find and store the char occurrences of the string (this can done by using a list containing 26 ints), convert this list to a tuple (call it curr_str_char_occurrences_tuple) instead of a list so it is immutable. (and thus will have a consistent hash). 
- Check and see if curr_str_char_occurrences_tuple is in grouped_anagrams as a key. If it is, add the currently iterated string in strs to the list which is stored as the key's associated value. If it is not, add curr_str_char_occurrences_tuple as a key in grouped_anagrams with the associated value being a list containing currently iterated string in strs.
- The return value will be a list of all the values stored in grouped_anagrams.

Notes:
- Creating a char occurrence using a 26-char list approach in order to sort through the chars of a string can bring our Sorting TC to O(n)

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

    # Solution 2
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}

        for curr_str in strs:
            curr_str_char_occurrences = [0] * 26

            for curr_char in curr_str:
                curr_str_char_occurrences[ord(curr_char) - 97] += 1
            
            curr_str_char_occurrences_tuple = tuple(curr_str_char_occurrences)

            if curr_str_char_occurrences_tuple in grouped_anagrams:
                grouped_anagrams[curr_str_char_occurrences_tuple].append(curr_str)
            else:
                grouped_anagrams[curr_str_char_occurrences_tuple] = [curr_str]

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
