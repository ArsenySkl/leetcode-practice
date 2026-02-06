# Задача: Longest Common Substring (упрощенная версия)
# Сложность: Medium/Hard

# Напишите функцию, чтобы найти самую длинную общую подстроку среди всех строк в массиве. Подстрока должна быть непрерывной последовательностью символов.

# Примеры:
# Пример 1:

# text
# Ввод: strs = ["abcdef", "abczyx", "abctuv"]
# Вывод: "abc"
# Объяснение: "abc" - самая длинная общая подстрока
# Пример 2:

# text
# Ввод: strs = ["flower", "flow", "flight"]
# Вывод: "fl"
# Пример 3:

# text
# Ввод: strs = ["dog", "racecar", "car"]
# Вывод: ""
# Объяснение: Нет общей подстроки
# Пример 4:

# text
# Ввод: strs = ["hello", "hell", "helmet", "shell"]
# Вывод: "hel"
# Пример 5:

# text
# Ввод: strs = ["programming", "grammar", "diagram"]
# Вывод: "gram"
# Ограничения:
# 1 <= strs.length <= 100

# 0 <= strs[i].length <= 100

# strs[i] состоит только из строчных английских букв

def find_longest_common_substring(strs):
    if not strs:
        return ""
    first_word = strs[0]
    new_str = first_word[0]
    # revers_first_word = ''.join([char for char in first_word[::-1]])
    # print(first_word)
    # print(revers_first_word)
    # for word in strs[1:]:
    #     while first_word not in word:
    #         print(word, first_word)
    #         if word.startswith(first_word):
    #             first_word = first_word[:-1]
    #         elif word.endswith(first_word):
    #             first_word = first_word[1:]
    #         else:

    for word in strs[1:]:
        while first_word not in word:
            for char in first_word:
                if new_str in word:
                    break
                else:
                    new_str += char

    return first_word


    


def main():
    print(find_longest_common_substring(["abcdef", "abczyx", "abctuv"]))

if __name__ == "__main__":
    main()