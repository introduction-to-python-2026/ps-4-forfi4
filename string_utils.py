def split_at_first_digit(formula):
    
    digit_location = -1

    for i in range(1, len(formula)):
        char = formula[i]
        if char.isdigit():
            # If a digit is found, record its index and stop
            digit_location = i
            break
            
    # 3. Check for Digit
    if digit_location == -1:
        # No digit was found (or string was 0-1 chars)
        # We also need to check if the *first* char is a digit
        if len(formula) > 0 and formula[0].isdigit():
             return ("", int(formula))
        # Otherwise, no digits were found
        return (formula, 1)
    else:
        # A digit was found at digit_location
        prefix = formula[:digit_location]
        number_str = formula[digit_location:]
        return (prefix, int(number_str))

def split_before_each_uppercases(formula):
    """
    Splits a string before each uppercase letter,
    returning a list of substrings.
    """
    # Handle Test 5: Empty string
    if not formula:
        return []

    # 1. Initialize arguments
    start = 0
    split_formula = []
    
    # 2. Loop through the string (starting from the second character)
    for end in range(1, len(formula)):
        # 3. Check for uppercase letters
        char = formula[end]
        if char.isupper():
            # 4. Update the list
            split_formula.append(formula[start:end])
            start = end
            
    # 5. Return the list (Append the last part)
    # After the loop, append the final remaining part
    split_formula.append(formula[start:])
    
    return split_formula
