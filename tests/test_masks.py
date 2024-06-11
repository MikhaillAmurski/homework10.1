from src.masks import card_number_hider, account_number_hider


def test_card_number_hider(num_card, num_error):
    assert card_number_hider(7000792289606361) == num_card
    assert card_number_hider(123) == num_error


def test_account_number_hider(num_account):
    assert account_number_hider(73654108430135874305) == num_account
