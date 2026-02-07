# 28. Find the Index of the First Occurrence in a String
# Easy

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

def find_index_first_occurence_in_string(haystack: str, needle: str):
    if needle not in haystack:
        return -1

    haystack_tmp = haystack
    for index in range(len(haystack)):
        if haystack_tmp.startswith(needle):
            return index
        else:
            haystack_tmp = haystack_tmp[1:]

def main():
    print(find_index_first_occurence_in_string(haystack = "sadbutsad", needle = "sad"))
    print(find_index_first_occurence_in_string(haystack = "adbutsad", needle = "sad"))
    print(find_index_first_occurence_in_string(haystack = "leetcode", needle = "leeto"))

if __name__ == '__main__':
    main()