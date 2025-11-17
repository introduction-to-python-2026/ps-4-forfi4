import re

def split_at_digit(formula: str):
    """
    Splits a string into a prefix (before the first digit) and
    a number (from the first digit onward).

    If no digits are found, returns the original string and 1.

    Args:
        formula: The input string (e.g., "H2O", "NaCl").

    Returns:
        A tuple of (prefix, number), where prefix is a string
        and number is an integer.
    """
    prefix = ""
    number_str = ""
    
    # Find the index of the first digit
    first_digit_index = -1
    for i, char in enumerate(formula):
        if char.isdigit():
            first_digit_index = i
            break
    
    # Case 1: No digit found
    if first_digit_index == -1:
        return (formula, 1)
    
    # Case 2: Digit found
    prefix = formula[:first_digit_index]
    number_str = formula[first_digit_index:]
    
    # Handle empty prefix (e.g., if string starts with a digit)
    if not prefix:
        # As per the logic, the part *before* the digit is the prefix.
        # If the string is "22", prefix is "" and number is 22.
        pass
        
    try:
        number = int(number_str)
        return (prefix, number)
    except ValueError:
        # This case should technically not be hit if .isdigit() is used,
        # but it's good practice.
        return (formula, 1)

def split_before_each_uppercase(formula: str):
    """
    Splits a string before every uppercase letter, keeping the
    uppercase letter as part of the following split.

    Args:
        formula: The input string (e.g., "NaCl", "C6H12O6").

    Returns:
        A list of strings.
    """
    if not formula:
        return []

    # A more robust way using regex:
    # Find all uppercase letters that are not at the start of the string
    # and use a positive lookahead to split *before* them.
    # [A-Z] matches an uppercase letter.
    # (?=...) is a positive lookahead, it asserts that what follows
    # matches, but doesn't consume the characters.
    # This splits the string at the boundary *before* an uppercase letter.
    # The filter(None, ...) removes any empty strings that might result
    # from the split (e.g., if the string starts with an uppercase letter).
    
    # Simpler logic without regex:
    parts = []
    current_part = ""
    for char in formula:
        if char.isupper():
            # If it's uppercase, and we have a current_part,
            # it means we've found the start of a new part.
            if current_part:
                parts.append(current_part)
            # Start the new part with this uppercase letter
            current_part = char
        else:
            # If not uppercase, just add it to the current part
            current_part += char
            
    # After the loop, add the last remaining part
    if current_part:
        parts.append(current_part)
        
    return parts
