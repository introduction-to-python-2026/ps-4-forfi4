def split_at_digit(formula):
    """
    Splits a string into:
      - prefix: everything before the first digit
      - number: the first digit onward as an integer

    If no digits exist, returns (formula, 1)
    """
    prefix = ""
    number_part = ""
    found_digit = False

    for ch in formula:
        if not found_digit and ch.isdigit():
            found_digit = True
        if found_digit:
            number_part += ch
        else:
            prefix += ch

    if number_part:
        return prefix, int(number_part)
    else:
        return formula, 1


def split_before_each_uppercase(formula):
    """
    Splits a string before every uppercase letter, keeping the uppercase letters
    in the resulting parts.

    Examples:
    >>> split_before_each_uppercase("NaCl") → ['Na', 'Cl']
    >>> split_before_each_uppercase("C6H12O6") → ['C6', 'H12', 'O6']
    """
    if not formula:
        return []

    parts = []
    current = formula[0]

    for ch in formula[1:]:
        if ch.isupper():
            parts.append(current)
            current = ch
        else:
            current += ch

    parts.append(current)
    return parts
