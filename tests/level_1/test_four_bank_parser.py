import datetime
from decimal import Decimal

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import pytest


cards = [
    [BankCard(last_digits="1234", owner="Ivan Ivanov")],
    [BankCard(last_digits="", owner="Ivan Ivanov")]
]

sms = SmsMessage(
    text="Purchase 1500.50 RUB, *1234 03.03.26 14:35 Supermarket authcode 123456",
    author="INECO",
    sent_at=datetime.datetime(2026, 3, 3, 14, 35),
)

expense = Expense(
    amount=Decimal('1500.50'),
    card=BankCard(
        last_digits='1234',
        owner='Ivan Ivanov'
    ),
    spent_in='Supermarket',
    spent_at=datetime.datetime(2026, 3, 3, 14, 35)
)



@pytest.mark.parametrize("test_input_1, test_input_2, expected",
                         [
                             (sms, cards[0], expense),
                             pytest.param(sms, cards[1], expense, marks=pytest.mark.xfail)
                         ], ids=["Normal test", "IndexError: Card number is None"])
def test_parse_ineco_expense(test_input_1, test_input_2, expected):
    assert parse_ineco_expense(test_input_1, test_input_2) == expected
