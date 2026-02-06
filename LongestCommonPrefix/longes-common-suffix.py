# Задача: Longest Common Suffix
# Сложность: Medium

# Описание
# Напишите функцию, чтобы найти самый длинный общий суффикс (окончание) среди массива строк.

# Если общего суффикса нет, верните пустую строку "".

# Примеры:
# Пример 1:

# text
# Ввод: strs = ["running", "jumping", "sleeping"]
# Вывод: "ing"
# Объяснение: Все слова оканчиваются на "ing"
# Пример 2:

# text
# Ввод: strs = ["cat", "dog", "bird"]
# Вывод: ""
# Объяснение: Нет общего суффикса
# Пример 3:

# text
# Ввод: strs = ["identical", "rical", "cal"]
# Вывод: "cal"
# Пример 4:

# text
# Ввод: strs = ["programmer", "gamer", "timer"]
# Вывод: "mer"
# Ограничения:
# 1 <= strs.length <= 200

# 0 <= strs[i].length <= 200

# strs[i] состоит только из строчных английских букв, если она не пустая

def find_longest_common_suffix(strs):
    if not strs:
        return ""
    
    first_word = strs[0]
    for word in strs[1:]:
        while not word.endswith(first_word):
            first_word = first_word[1:]
    return first_word


def main():
    print(find_longest_common_suffix(["running", "jumping", "sleeping"]))
    print(find_longest_common_suffix(["cat", "dog", "bird"]))
    print(find_longest_common_suffix(["identical", "rical", "cal"]))
    print(find_longest_common_suffix(["programmer", "gamer", "timer"]))

if __name__ == '__main__':
    main()