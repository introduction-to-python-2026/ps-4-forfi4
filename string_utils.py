import string

def split_at_digit(formula):
    """
    Splits a string into a prefix (before the first digit) and the rest 
    as an integer (from the first digit onward).

    If no digit is found, returns the original string and the integer 1.
    Uses a loop to find the split point.
    """
    first_digit_index = -1
    
    # Use a loop to find the index of the first character that is a digit
    for i in range(len(formula)):
        if formula[i].isdigit():
            first_digit_index = i
            break  # Exit the loop as soon as the first digit is found

    if first_digit_index == -1:
        # Case 1: No digits found
        return (formula, 1)
    else:
        # Case 2: Digit found. Split the string.
        prefix = formula[:first_digit_index]
        number_str = formula[first_digit_index:]
        # Convert the number part to an integer
        number = int(number_str)
        return (prefix, number)


def split_before_each_uppercase(formula):
    """
    Splits a string before every uppercase letter. 
    Keeps the uppercase letters as the start of the new chunk.
    Uses a loop to iterate and build the chunks.
    """
    if not formula:
        return []

    result = []
    # Start the first chunk with the very first character
    current_chunk = formula[0] 

    # Loop through the string starting from the second character (index 1)
    for i in range(1, len(formula)):
        char = formula[i]

        if char.isupper():
            # This is the start of a new element.
            # 1. Save the chunk we just finished.
            result.append(current_chunk)
            # 2. Start the new chunk with the current uppercase letter.
            current_chunk = char
        else:
            # Continue building the current chunk.
            current_chunk += char

    # After the loop, add the very last chunk to the result list
    if current_chunk:
        result.append(current_chunk)

    return result

