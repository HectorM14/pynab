from datetime import date


test_month = date(2015, 9, 1)


def test_get_monthly_budgets(budget):
    # ensure the monthly budgets contains our test month
    assert test_month in [mb.month for mb in budget.monthly_budgets]


def test_filtering_on_month(budget):
    res = budget.monthly_budgets.filter('month', test_month)
    assert len(res) == 1
    assert res[0].month == test_month


def test_get_budgeted_amounts(budget):
    september = budget.monthly_budgets.filter('month', test_month)[0]
    category_budgets = september.monthly_sub_category_budgets
    category_full_name_to_budgeted_amount = dict((cb.category.full_name, cb.budgeted) for cb in category_budgets)
    assert category_full_name_to_budgeted_amount['Master category 1/subcategory B'] == 20.0
    assert category_full_name_to_budgeted_amount['Master category 1/subcategory A'] == 10.0
    assert category_full_name_to_budgeted_amount['Master category 2/subcategory B'] == 40.0
    assert category_full_name_to_budgeted_amount['Master category 2/subcategory A'] == 30.0


def test_overspend_handling(budget):
    september = budget.monthly_budgets.filter('month', test_month)[0]
    category_budgets = september.monthly_sub_category_budgets
    category_full_name_to_overspend_handling = dict((cb.category.full_name, cb.overspending_handling)
                                                    for cb in category_budgets)
    assert category_full_name_to_overspend_handling['Master category 2/subcategory B'] == None
    # Confined means the overspending is confined to that category
    assert category_full_name_to_overspend_handling['Master category 2/subcategory A'] == 'Confined'


def test_can_access_budget_though_category(budget):
    c = budget.categories.filter('full_name', 'Master category 1/subcategory B')[0]
    mb = c.monthly_sub_category_budgets[0]
    assert mb.month == test_month
    assert mb.budgeted == 20