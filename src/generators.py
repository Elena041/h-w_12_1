from typing import Any, Dict, Generator, List


def filter_by_currency(transactions: list[Dict[Any, Any]], currency: str) -> Generator[dict, None, None]:

    """
    Функция-генератор, которая принимает список словарей с банковскими операциями
    и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта
    Аргументы:
        transactions (List[Dict]): Список словарей с банковскими операциями.
        currency (str): Валюта, по которой нужно фильтровать операции.
    """
    for key in transactions:
        if key["operationAmount"]["currency"]["code"] == currency:
            yield key


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """Функция-генератор, которая принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Функция-генератор номеров банковских карт, который генерирует номера карт в формате
    XXXX XXXX XXXX XXXX,где Х - это цифра.
    Пример вывода от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    for number in range(start, stop + 1):
        card_number = f"{number:016}"  # Форматируем номер как 16-значное число с лидирующими нулями
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number
