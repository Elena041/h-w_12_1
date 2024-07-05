from typing import Dict
import json
import logging

def get_way_from_tranzactions(json_info: str) -> list[Dict]:
    """ Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
