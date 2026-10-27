"""
Two Sum
https://leetcode.com/problems/two-sum/

Дано: список чисел nums и цель target.
Надо: вернуть индексы двух чисел, сумма которых равна target.
"""


# Input: nums = [2,7,11,15], target = 9
#
# Output: [0,1]


def two_sum(nums: list[int], target: int) -> list[int]:
    for index in range(len(nums)):  # Первый индекс
        for j in range(index + 1, len(nums)):  # Второй индекс (только после i)
            if nums[index] + nums[j] == target:  # Проверяем сумму
                return [index, j]   # Нашли — возвращаем индексы
        return []    # Если не нашли — пустой


print(two_sum([7, 2, 11, 15], 9))
