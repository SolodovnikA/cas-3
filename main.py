import local


def tax_lonely(income_t):
    tax = 0
    if income_t <= 9075:
        tax = income_t * 0.1
    elif 9076 >= income_t <= 36900:
        tax = 9076 * 0.1 + (income_t - 9076) * 0.15
    elif 36901 >= income_t <= 89350:
        tax = 9076 * 0.1 + (36900 - 9076) * 0.15 + (income_t - 36901) * 0.25
    elif 89351 >= income_t <= 186350:
        tax = 9076 * 0.1 + (36900 - 9076) * 0.15 + (89350 - 26901) * 0.25 + (income_t - 89351) * 0.28
    elif 186351 >= income_t <= 405100:
        tax = 9076 * 0.1 + (36900 - 9076) * 0.15 + (89350 - 26901) * 0.25 + (186350 - 89351) * 0.28 + (
                    income_t - 186351) * 0.33
    elif income_t >= 406751:
        tax = 9076 * 0.1 + (36900 - 9076) * 0.15 + (89350 - 26901) * 0.25 \
              + (186350 - 89351) * 0.28 + (405100 - 186351) * 0.33 + (income_t - 406751) * 0.396
    return tax


if __name__ == '__main__':  # Run only if this file is active
    tax_type = int(input(local.question_1))

    incomes_for_tax = []

    for month in local.months:
        income_for_tax = int(input(local.question_2 + month + '\n'))
        income_with_out_tax = int(input(local.question_2 + month + '\n'))
        incomes_for_tax.append(income_for_tax - income_with_out_tax)

    if tax_type == 1:
        year_taxes = 0
        for income_for_tax in incomes_for_tax:
            year_taxes += tax_lonely(income_for_tax)

        print(year_taxes)
