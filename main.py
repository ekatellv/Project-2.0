# Part of a case-study #2: Credits
# Developers: Loseva Ekaterina, Shcherbina Ekaterina
#

import ru_local as ru

def main():
    '''
    Main function.
    :return: None
    '''

    loan_amount = int(input(ru.SUM_LOAN))
    loan_payment_1 = int(input(ru.F_PAYMENT))
    loan_payment_2 = int(input(ru.S_PAYMENT))

    if loan_amount <= 0 or loan_payment_1 <= 0 or loan_payment_2 <= 0 \
        or loan_payment_1 + loan_payment_2 < loan_amount \
        or loan_payment_1 ** 2 + (4 * loan_amount * loan_payment_2 ) < 0:
        print(f'{ru.FALSE_VALUES}')
    else:
        # finding solutions to the quadratic equation
        # interest_coef = 1 + 0,01 * interest_rate!!!!!111111111dddddd
        interest_coef_1 = (loan_payment_1 + (loan_payment_1 ** 2 + 4 * loan_amount * loan_payment_2) ** 0.5) / (2 * loan_amount)
        interest_coef_2 = (loan_payment_1 - (loan_payment_1 ** 2 + 4 * loan_amount * loan_payment_2) ** 0.5) / (2 * loan_amount)
        interest_rate = round((max(interest_coef_1, interest_coef_2) - 1) * 100, 2)

        print(f'{ru.INTEREST}, {interest_rate}')

        loan_payment_max = int(input(ru.MAX_PAYMENT))

        if loan_payment_max <= 0 or loan_payment_max > loan_amount:
            print(f'{ru.FALSE_VALUES}')
        else:
            loan_term = 0
            while loan_amount > 0:
                loan_amount = loan_amount * (1 + 0.01 * interest_rate) - loan_payment_max
                loan_term += 1

            print(f'{ru.MIN_YEARS}, {loan_term}')


if __name__ == '__main__':
    main()
