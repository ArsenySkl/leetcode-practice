# Задача 1: "Two Sum — разные индексы"
# Дана модификация:
# На входе два отдельных массива nums1 и nums2 и число target.
# Нужно вернуть индексы [i, j] такие, что nums1[i] + nums2[j] == target.
# Если есть несколько решений — вернуть первое найденное.

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# target = 7
# Возможные ответы: [0, 1] (1 + 6 = 7) или [1, 0] (2 + 5 = 7) или [2, 0] (3 + 4 = 7)

def two_sum_diff_index_optimised(nums1, nums2, target):
    dict_nums1 = {}
    for index, num1 in enumerate(nums1):
        dict_nums1[num1] = index
    
    for index, num2 in enumerate(nums2):
        diff = target - num2
        if diff in dict_nums1:
            return [dict_nums1[diff], index]
    return

def two_sum_diff_index(nums1, nums2, target):
    for index1, num1 in enumerate(nums1):
        for index2, num2 in enumerate(nums2):
            if num1 + num2 == target:
                return [index1, index2]
    return None

def main():
    print(two_sum_diff_index([1, 2, 3], [4, 5, 6], 7))
    print(two_sum_diff_index_optimised([1, 2, 3], [4, 5, 6], 7))

if __name__ == '__main__':
    main()