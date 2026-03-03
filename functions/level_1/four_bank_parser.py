import datetime
import decimal
from typing import NamedTuple


class BankCard(NamedTuple):
    last_digits: str
    owner: str


class SmsMessage(NamedTuple):
    text: str
    author: str
    sent_at: datetime.datetime


class Expense(NamedTuple):
    amount: decimal.Decimal
    card: BankCard
    spent_in: str
    spent_at: datetime.datetime


def parse_ineco_expense(sms: SmsMessage, cards: list[BankCard]) -> Expense:
    """
    Вычисление денежных трат и обстоятельства, при которых деньги были потрачены.

    Пример:
    cards = [
        BankCard(last_digits="1234", owner="Ivan Ivanov"),
    ]

    sms = SmsMessage(
        text="Purchase 1500.50 RUB, *1234 03.03.26 14:35 Supermarket authcode 123456",
        author="INECO",
        sent_at=datetime.datetime.now(),
    )

    parse_ineco_expense(sms, cards) -> Expense(
                                                amount=Decimal('1500.50'),
                                                card=BankCard(
                                                    last_digits='1234',
                                                    owner='Ivan Ivanov'
                                                ),
                                                spent_in='Supermarket',
                                                spent_at=datetime.datetime(2026, 3, 3, 14, 35)
                                            )
    """

    raw_sum, raw_details = sms.text.split(', ')
    raw_details = raw_details.split(' authcode ')[0]
    raw_card, raw_date, raw_time, spend_in = raw_details.split(' ', maxsplit=3)
    return Expense(
        amount=decimal.Decimal(raw_sum.split(' ')[-2]),
        card=[c for c in cards if c.last_digits == raw_card[-4:]][0],
        spent_in=spend_in,
        spent_at=datetime.datetime.strptime(f'{raw_date} {raw_time}', '%d.%m.%y %H:%M'),
    )
