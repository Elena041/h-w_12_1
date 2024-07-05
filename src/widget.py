from src.masks import get_masks_nums


def hide_card_details(nums: str) -> str:
    """Функция, которая маскирует номер карты/счета"""
    card_parts = nums.split()
    card_parts[-1] = get_masks_nums(card_parts[-1])

    return " ".join(card_parts)


def get_date(date: str) -> str:
    """Функция для форматирования даты"""

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
