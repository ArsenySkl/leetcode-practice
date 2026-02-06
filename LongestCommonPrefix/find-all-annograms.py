# Задача: Find All Anagrams in Word
# Сложность: Medium

# Напишите функцию, которая находит все анаграммы заданного слова в списке слов. 
# Анаграмма - это слово, составленное из тех же букв, что и исходное, но в другом порядке (регистр не учитываем).

# Примеры:
# Пример 1:

# python
# find_anagrams("listen", ["enlists", "google", "inlets", "banana"])
# # → ["inlets"]
# # "inlets" состоит из тех же букв, что и "listen"
# Пример 2:

# python
# find_anagrams("cat", ["act", "tac", "dog", "god", "tca"])
# # → ["act", "tac", "tca"]
# Пример 3:

# python
# find_anagrams("hello", ["helol", "olelh", "world", "llohe"])
# # → ["helol", "olelh", "llohe"]
# Пример 4:

# python
# find_anagrams("python", ["typhon", "nythop", "java", "nohtyp"])
# # → ["typhon", "nythop", "nohtyp"]
# Пример 5:

# python
# find_anagrams("a", ["a", "b", "aa"])
# # → ["a"]
# Ограничения:
# Все слова состоят из строчных английских букв

# 1 <= len(word) <= 100

# 0 <= len(word_list) <= 1000

def find_anagrams(word, word_list):
    count = []
    # tmp_word = word
    for item in word_list:
        tmp_word = word
        # print(len(word), len(item))
        if len(word) != len(item):
            continue
        for char in item:
            if char in tmp_word:
                tmp_word = tmp_word.replace(char, '', 1)
                # print(tmp_word)
            if len(tmp_word) == 0:
                count.append(item)
    return count

def main():
    print(find_anagrams("listen", ["enlists", "google", "inlets", "banana"]))
    print(find_anagrams("cat", ["act", "tac", "dog", "god", "tca"]))
    print(find_anagrams("hello", ["helol", "olelh", "world", "llohe"]))
    print(find_anagrams("python", ["typhon", "nythop", "java", "nohtyp"]))
    print(find_anagrams("a", ["a", "b", "aa"]))
    print(find_anagrams("aab", ["aba", "abb", "baa"]))

main()