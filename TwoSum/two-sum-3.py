# Задача 2: "Two Sum — уже отсортированный массив"
# Массив nums отсортирован по возрастанию.
# Найти индексы двух чисел, дающих в сумме target.
# Можно ли решить без доп. памяти (O(1) памяти), но быстрее O(n²)?

# Пример:

# text
# nums = [2, 7, 11, 15]
# target = 9
# Ответ: [0, 1]

def two_sum(nums, target):
    dict_nums = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in dict_nums:
            return [dict_nums[diff], index]
        dict_nums[num] = index

def main():
    print(two_sum([2, 7, 11, 15], 9))

if __name__ == '__main__':
    main()