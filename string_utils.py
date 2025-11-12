import string

def split_at_digit(formula):
    """
    Splits a string into a prefix (before the first digit) and the rest 
    as an integer (from the first digit onward).

    If no digit is found, returns the original string and the integer 1.
    Uses a loop to find the split point.
    """
    first_digit_index = -1
    
    # 1. Use a loop to find the index of the first character that is a digit
    for i in range(len(formula)):
        if formula[i].isdigit():
            first_digit_index = i
            break  # Exit the loop as soon as the first digit is found

    if first_digit_index == -1:
        # Case 1: No digits found
        return (formula, 1)
    else:
        # Case 2: Digit found. Find the end of the consecutive number part.
        
        # We start looking for the end of the number right after the first digit
        end_of_number_index = first_digit_index
        
        # Loop forward from the start of the number until a non-digit is hit
        for j in range(first_digit_index, len(formula)):
            if formula[j].isdigit():
                # If it's a digit, extend the end index
                end_of_number_index = j + 1
            else:
                # If it's not a digit (e.g., 'B' in "A9B1C2"), stop the number extraction
                break 
        
        # Prefix is everything before the first digit
        prefix = formula[:first_digit_index]
        
        # Number string is only the CONSECUTIVE digits
        number_str = formula[first_digit_index:end_of_number_index]
        
        # Convert the clean digit string to an integer
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
    
    # Handle the edge case where the formula is not empty but formula[0] might cause 
    # an IndexError if formula is an empty string, though the 'if not formula' handles it.
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

