import local


def tax_lonely(x):
    tax = 0
    if x <= 9075:
        tax = x * 0.1
    elif 9076 >= x <= 36900:
        tax = 9075 * 0.1 + (x - 9076) * 0.15
    elif 36901 >= x <= 89350:
        tax = 9075 * 0.1 + (36900 - 9076) * 0.15 + (x - 36901) * 0.25
    elif 89351 >= x <= 186350:
        tax = 9075 * 0.1 + (36900 - 9076) * 0.15 + (89350 - 36901) * 0.25 + (x - 89351) * 0.28
    elif 186351 >= x <= 405100:
        tax = 9075 * 0.1 + (36900 - 9076) * 0.15 + (89350 - 36901) * 0.25 + (186350 - 89351) * 0.28 + (
                    x - 186351) * 0.33
    elif 405101 >= x <= 406750:
        tax = 9075 * 0.1 + (36900 - 9076) * 0.15 + (89350 - 36901) * 0.25 + (186350 - 89351) * 0.28 + (
                405100-186351) * 0.33 + (x - 405101)*0.35
    elif x >= 406751:
        tax = 9075 * 0.1 + (36900 - 9076) * 0.15 + (89350 - 36901) * 0.25 + (186350 - 89351) * 0.28 + (
                405100-186351) * 0.33 + (406750 - 405101)*0.35 + (x - 406751) * 0.396
    return tax


if __name__ == '__main__':  # Run only if this file is active
    tax_type = int(input(local.QUESTION_1))

    income = 0
    for month in local.MONTHS:
        print(local.REQUEST_1, end='\n')
        income_for_tax = int(input(local.QUESTION_2 + month + '\n'))
        income += income_for_tax
    print(local.INCOME_SUMMARY + income, end='\n')

    income_free_tax = 0
    for month in local.MONTHS:
        print(local.REQUEST_2, end='\n')
        income_without_tax = int(input(local.QUESTION_3 + month + '\n'))
        income_free_tax += income_without_tax
    print(local.INCOME_FREE + income_free_tax, end='\n')

    income_t = income - income_free_tax
    print(local.FINAL_INCOME + income_t, end='\n')

    if tax_type == 1:
        print(local.YEARLY_TAX + tax_lonely(income_t))
        print(local.MONTHLY + tax_lonely(income_t)/12)

        # print(year_taxes)
