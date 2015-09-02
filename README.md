# pYNAB

A minimalistic library designed to provide native access to YNAB data from Python.

# Install

The simplest way is to install the latest version from PyPI index:

```sh
> pip install -U pynab
```

or install from the latest source:

```sh
git clone https://github.com/aldanor/pynab.git
cd pynab
python setup.py install
```

# Examples

Load the shared YNAB budget:

```python
>>> from ynab import YNAB
>>> budget = YNAB('~/Dropbox/YNAB', 'MyBudget')
```

Get the list of accounts:

```python
>>> budget.accounts
[<Account: Cash>, <Account: Checking>]
```

Query the balance, the cleared balance and the reconciled balance for cash account:

```python
>>> cash = budget.accounts['Cash']
>>> cash.balance, cash.cleared_balance, cash.reconciled_balance
(15.38, 24.38, 41.88)
```

Find the total of all reconciled cash transactions starting 2 weeks ago:

```python
>>> cash = budget.accounts['Cash']
>>> sum(cash.transactions.since('2 weeks ago').filter('reconciled').amount)
-22.0
```

Find the average amount of all Starbucks purchases in 2015:

```python
>>> starbucks = budget.payees['Starbucks']
>>> starbucks.transactions.between('2015-01-01', '2015-12-31').amount.mean()
-27.31176470588235
```

# Monthly budgets

Query the monthly budgets month by month

```python
>>> monthly_budgets = budget.monthly_budgets
>>> a_budget = monthly_budgets[0]
>>> a_budget.month
u'2014-05-01'
# pick out a random category from this month to use as an example
>>> coffee_jan_14 = a_budget.monthly_sub_category_budgets[0]
>>> coffee_jan_14.budgeted
20.0
>>> coffee_jan_14.category
<Category: Food & Drink/Coffee>
```

Or query them by category

```python
>>> categories = budget.categories
>>> a_category = categories[0]
>>> a_category
<Category: Food & Drink/Coffee>
>>> a_budgeted_amount = a_category.monthly_sub_category_budgets[0]
>>> a_budgeted_amount.month
u'2014-05-01'
>>> a_budgeted_amount.budgeted
20.0
```