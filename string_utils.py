def split_at_first_digit(formula):
    digit_location = 1 

    # Loop through characters starting from the second one (index 1)
    for char_index_offset, char in enumerate(formula[1:]):
        if char.isdigit():
            # If a digit is found, break. digit_location already holds the correct index.
            break
        digit_location += 1 # Increment digit_location for the next character in formula[1:]

    # After the loop, digit_location holds the index of the first digit
    # OR if no digit was found in formula[1:], it will be len(formula).

    # Check if digit_location has reached the end of the formula.
    # This implies no digit was found from index 1 onwards.
    if digit_location == len(formula):
        # According to the problem: "If no digit is found, return the original string and 1 as the number."
        return (formula, 1)
    else:
        # A digit was found at digit_location.
        # Split the formula into prefix and numeric part.
        prefix = formula[:digit_location]
        numeric_part = int(formula[digit_location:])
        return (prefix, numeric_part)
def split_before_each_uppercases(formula):
    split_formula = []
    start = 0
    
    if not formula:
        return []

    for end in range(1, len(formula)):
        if formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end
    
    # Append the last part of the string after the loop
    split_formula.append(formula[start:])
    return split_formula  # Ensure this line uses a standard space
