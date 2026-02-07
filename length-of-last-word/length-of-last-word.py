# 58. Length of Last Word
# Easy

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

def length_of_last_word(s: str):
    print(s)
    print(list(s))
    # list_s = list(s)
    # tmp_s = s
    # count = 0
    count_len = 0
     # Идем с конца строки
    for i in range(len(s) - 1, -1, -1):
        # Пропускаем пробелы в конце
        if s[i] == ' ' and count_len == 0:
            continue
        # Нашли не-пробел - начинаем считать
        elif s[i] != ' ':
            count_len += 1
        # Встретили пробел после слова - заканчиваем
        else:
            break
    return count_len


def main():
    print(length_of_last_word(s = "Hello World"))
    print(length_of_last_word(s = "   fly me   to   the moon  "))
    print(length_of_last_word(s = "luffy is still joyboy"))

if __name__ == '__main__':
    main()