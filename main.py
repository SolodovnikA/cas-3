import local as ru


def tax_lonely(x):
    """
    Function determines amount of yearly tax for a single person
    """
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


def one_parent(x):
    tax = 0
    if x <= 12950:
        tax = x * 0.1
    elif 12951 >= x <= 49400:
        tax = 12950 * 0.1 + (x - 12951) * 0.15
    elif 49401 >= x <= 127550:
        tax = 12950 * 0.1 + (49400 - 12951) * 0.15 + (x - 49401) * 0.25
    elif 127551 >= x <= 206600:
        tax = 12950 * 0.1 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (x - 127551) * 0.28
    elif 206601 >= x <= 405100:
        tax = 12950 * 0.1 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (206600 - 127551) * 0.28 + (
                    x - 206601) * 0.33
    elif 405101 >= x <= 432200:
        tax = 12950 * 0.1 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (206600 - 127551) * 0.28 + (
                405100-206601) * 0.33 + (x - 405101)*0.35
    elif x >= 432201:
        tax = 12950 * 0.1 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (206600 - 127551) * 0.28 + (
                405100-206601) * 0.33 + (432200 - 405101)*0.35 + (x - 432201) * 0.396
    return tax
def family(x):
    tax = 0
    if x <= 18150:
        tax = x * 0.1
    elif 18151 >= x <= 73800:
        tax = 18150 * 0.1 + (x - 18151) * 0.15
    elif 73801 >= x <= 148850:
        tax = 18150 * 0.1 + (73800-18151) * 0.15 + (x - 73801) * 0.25
    elif 148851 >= x <= 226850:
        tax = 18150 * 0.1 + (73800 - 18151) * 0.15 + (148850-73801) * 0.25+(x-148851)*0.28
    elif 226851 >= x <= 405100:
        tax = 18150 * 0.1 + (73800 - 18151) * 0.15 + (148850 - 73801) * 0.25 + (226850 - 148851) * 0.28 + (
            x - 226851)*0.33
    elif 405101 >= x <= 457600:
        tax = 18150 * 0.1 + (73800 - 18151) * 0.15 + (148850 - 73801) * 0.25 + (226850 - 148851) * 0.28 + (
                405100 - 226851) * 0.33 + (x - 405101) * 0.35
    elif x >= 457601:
        tax = 18150 * 0.1 + (73800 - 18151) * 0.15 + (148850 - 73801) * 0.25 + (226850 - 148851) * 0.28 + (
                405100 - 226851) * 0.33 + (457600 - 405101) * 0.35 + (x-457601)*0.396
        return tax


if __name__ == '__main__':  # Run only if this file is active
    tax_type = int(input(ru.QUESTION_1))

    income = 0
    for month in ru.MONTHS:
        print(ru.REQUEST_1)
        income_for_tax = int(input(ru.QUESTION_2 + month + '\n'))
        income += income_for_tax
    print(ru.INCOME_SUMMARY + income, end='\n')

    income_free_tax = 0
    for month in ru.MONTHS:
        print(ru.REQUEST_2)
        income_without_tax = int(input(ru.QUESTION_3 + month + '\n'))
        income_free_tax += income_without_tax
    print(ru.INCOME_FREE + income_free_tax, end='\n')

    income_t = income - income_free_tax
    print(ru.FINAL_INCOME + income_t, end='\n')

    if tax_type == 1:
        print(ru.YEARLY_TAX + tax_lonely(income_t))
        print(ru.MONTHLY + tax_lonely(income_t)/12)

    elif tax_type == 3:
        print(ru.YEARLY_TAX + one_parent(income_t))
        print(ru.MONTHLY + one_parent(income_t) / 12)
    else:
        print(ru.ERROR)
