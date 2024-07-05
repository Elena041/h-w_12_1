import json
from typing import Dict


def get_way_from_transactions(json_info: str) -> list[Dict]:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(json_info, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except json.JSONDecodeError:
        print("Неверный формат JSON.")
        return []


if __name__ == "__main__":
    file_path = "../data/operations.json"
    transactions = get_way_from_transactions(file_path)

    if transactions:
        print("Список транзакций:")
        for transaction in transactions:
            print(transaction)
    else:
        print("Файл не найден, пустой или содержит некорректный JSON.")
