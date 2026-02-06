# Сложность: Easy/Medium

# Напишите функцию, которая находит общие символы (буквы), которые присутствуют во всех словах. 
# Важно: если буква повторяется несколько раз в слове, то в ответе она должна повторяться столько раз, сколько минимально встречается во всех словах.

# Примеры:
# Пример 1:

# text
# Ввод: strs = ["bella", "label", "roller"]
# Вывод: ["e", "l", "l"]
# Объяснение: 
# - "e" есть во всех словах 1 раз минимум
# - "l" есть во всех словах минимум 2 раза
# Пример 2:

# text
# Ввод: strs = ["cool", "lock", "cook"]
# Вывод: ["c", "o"]
# Пример 3:

# text
# Ввод: strs = ["dog", "racecar", "car"]
# Вывод: []
# Пример 4:

# text
# Ввод: strs = ["a", "a", "a"]
# Вывод: ["a"]

def find_common_character(strs):
    first_word = strs[0]
    target = {}
    for char in first_word:
        # print(char)
        for word in strs:
            if char in word and word == first_word:
                # print(f"Это первое слово! встречается буква {char} в слове {word} столько раз: ", word.count(char))
                target[char] = word.count(char)
            elif char in word:
                if word.count(char) < target[char]:
                    target[char] = word.count(char)
                # print(f"встречается буква {char} в слове {word} столько раз: ", word.count(char))
            elif char not in word:
                # print(f"не встречается буква {char} и ее нет в слове {word} !")
                if char in target:
                    target.pop(char)
    print(target)
    # Преобразование словаря target в список
    result = []
    for char, count in target.items():
        result += [char] * count  # добавляем букву count раз
    return result


def main():
    print(find_common_character(["bella", "label", "roller"]))
    print(find_common_character(["cool", "lock", "cook"]))
    print(find_common_character(["dog", "racecar", "car"]))
    print(find_common_character(["a", "a", "a"]))

if __name__ == '__main__':
    main()