from datetime import datetime
import pdb


def validate_credit_card(card_number, expiry, cvv):
    # Remove non-digit characters from card number
    card_number = ''.join(filter(str.isdigit, card_number))

    # Check card number length and format
    if len(card_number) < 16 or len(card_number) > 19 or not card_number.isdigit():
        print("Wrong input size of Card Number")
        return False

    # Perform Luhn algorithm validation
    def luhn_check(card_number):
        digits = [int(digit) for digit in card_number]
        checksum = 0

        for i in range(len(digits) - 2, -1, -2):
            digit = digits[i]
            doubled_digit = digit * 2
            if doubled_digit > 9:
                doubled_digit -= 9
            digits[i] = doubled_digit

        checksum = sum(digits) % 10
        return checksum == 0

    if not luhn_check(card_number):
        print("Luhn Check Fail!")
        return False

    # Check expiration date format and validity
    try:
        expiry_month = int(expiry[:2])  # Gets expiry month
        expiry_year = int(expiry[2:])   # Gets expiry year
        current_year = datetime.now().year
        print(expiry_month)


        if expiry_year < current_year % 100 or (expiry_month < 1 or expiry_month > 12):
            print("Date Fail!")
            return False
    except ValueError:
        print("Erro ao converter valores de data em inteiros")

    # Check CVV length
    is_american_express = card_number.startswith(('34', '37'))
    if is_american_express and len(cvv) != 4:
        return False
    elif not is_american_express and len(cvv) != 3:
        print("Wrong CVV len!")
        return False

    return True

if __name__ == '__main__':
    pass
