# 14. Longest Common Prefix
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

def find_longest_prefix(strs):
    if not strs:  # если список пустой
        return ""
    
    # берем первое слово как начальный префикс
    prefix = strs[0]
    
    # проходим по всем остальным словам
    for word in strs[1:]:
        # укорачиваем префикс, пока он не станет началом текущего слова
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # убираем последний символ
            if not prefix:  # если префикс стал пустым
                return ""
    
    return prefix

def main():
    print(find_longest_prefix(["flower", "flow", "flight"]))  # fl
    print(find_longest_prefix(["dog", "racecar", "car"]))     # пустая строка
    print(find_longest_prefix(["interspecies", "interstellar", "interstate"]))  # inters
    print(find_longest_prefix(["interspecies", "intasderstellar", "interstate"]))  # inters

if __name__ == '__main__':
    main()