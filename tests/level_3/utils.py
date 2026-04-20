import decimal
from datetime import datetime

from functions.level_3.models import (
    Expense,
    BankCard,
    Currency,
    ExpenseCategory,
)

def make_expense(amount: float = 25, spent_in: str = None, spent_at: datetime = None) -> Expense:
    return Expense(
        amount=decimal.Decimal(str(amount)),
        currency=Currency.AMD,
        card=BankCard(last_digits="1234", owner="Tester"),
        spent_in=spent_in,
        spent_at=spent_at,
        category=ExpenseCategory.SUPERMARKET,
    )
