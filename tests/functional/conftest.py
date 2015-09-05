import pytest
from ynab import YNAB
import os


@pytest.yield_fixture(scope='session')
def budget():
    budget_path = os.path.join(os.path.dirname(__file__), 'test_budgets')
    budget = YNAB(budget_path, 'testing_budget')
    yield budget