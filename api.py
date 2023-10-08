def validate_credit_card(card_number, expiry, cvv):
    print(card_number)
    print(expiry)
    print(cvv)

    # Remove non-digit characters from card number
    card_number = ''.join(filter(str.isdigit, card_number))

    # Check card number length and format
    if len(card_number) < 16 or len(card_number) > 19 or not card_number.isdigit():
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
        return False

    # Check expiration date format and validity
    try:
        expiry_date = datetime.strptime(expiry, "%m/%y")
        current_date = datetime.now()
        if expiry_date < current_date or expiry_date.month < 1 or expiry_date.month > 12:
            return False
    except ValueError:
        return False

    # Check CVV length
    is_american_express = card_number.startswith(('34', '37'))
    if is_american_express and len(cvv) != 4:
        return False
    elif not is_american_express and len(cvv) != 3:
        return False

    return True

if __name__ == '__main__':
    pass
