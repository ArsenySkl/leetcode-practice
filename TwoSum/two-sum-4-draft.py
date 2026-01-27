# Задача: "Two Sum — с возможными дубликатами"
# Дана модификация задачи Two Sum:

# Массив nums может содержать дубликаты

# Нужно вернуть все уникальные пары индексов, дающие в сумме target

# Пары [i, j] и [j, i] считаются одинаковой парой (не дублировать)

# Индексы в паре должны быть разными (нельзя использовать один элемент дважды)

# Можно возвращать пары в любом порядке

# Пример 1:

# text
# nums = [1, 3, 2, 3, 4]
# target = 6
# Возможные решения:
# - nums[1] + nums[3] = 3 + 3 = 6 → [1, 3]
# - nums[2] + nums[4] = 3 + 3 = 6 → [2, 4]

# Но осторожно: nums[1] и nums[3] оба равны 3, но это разные элементы!
# Пример 2:

# text
# nums = [2, 2, 2, 2]
# target = 4
# Возможные пары индексов:
# [0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]

def two_sum_dedublicate(nums, target):
    dict_one = {}
    dict_result = []
    for index, num in enumerate(nums):
        diff = target - num
        if diff in dict_one:
            dict_result.append([dict_one[diff], index])
        if index not in dict_one.values():
            dict_one[num] = index
        print(dict_one)
    return dict_result

def main():
    print(two_sum_dedublicate([1, 3, 2, 3, 4], 6))
    print(two_sum_dedublicate([2, 2, 2, 2], 4))

if __name__ == '__main__':
    main()