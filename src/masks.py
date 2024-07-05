def masks_card_numbers(nums: str) -> str:
    """Функция, которая маскирует номер карты"""

    return f"{nums[:4]} {nums[4:6]}** **** {nums[-4:]}"


def masks_account_numbers(nums: str) -> str:
    """Функция, которая маскирует номер счета"""

    return f"**{nums[-4:]}"


def get_masks_nums(nums: int | str) -> str:
    """Функция, которая проверяет введеный номер"""

    nums = str(nums)
    if len(nums) == 16 and nums.isdigit():

        return masks_card_numbers(nums)

    elif len(nums) == 20 and nums.isdigit():

        return masks_account_numbers(nums)
    else:

        return "Некорректный ввод. Введите 16-ти или 20-ти-значное число."
