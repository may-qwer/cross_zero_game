array1 = [1, 3, 5, 6, 9]
array2 = [1, 5, 9]

set1 = set(array1)
set2 = set(array2)

common_nums = set1.intersection(set2)

if len(common_nums) > 0:
    print("Есть общие числа в массивах:")
    print(common_nums)
else:
    print("Общих чисел в массивах нет.")