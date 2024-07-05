from src.masks import get_masks_nums, masks_account_numbers, masks_card_numbers


def test_get_masks_nums():
    assert get_masks_nums(7000792289606361) == "7000 79** **** 6361"
    assert get_masks_nums(73654108430135874305) == "**4305"
    assert get_masks_nums("324fvdg") == "Некорректный ввод. Введите 16-ти или 20-ти-значное число."


def test_masks_account_numbers(account):
    assert masks_account_numbers("1234567898765432198") == account


def test_masks_card_numbers(card):
    assert masks_card_numbers("1652876337187398") == card
