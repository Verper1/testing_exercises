import collections
import decimal
from statistics import mean

from functions.level_3.models import Expense


def calculate_average_daily_expenses(expenses: list[Expense]) -> decimal.Decimal:
    total_expenses_by_day = collections.defaultdict(decimal.Decimal)

    for expense in expenses:
        total_expenses_by_day[expense.spent_at.date()] += expense.amount

    spam = mean(total_expenses_by_day.values())

    return spam
