def split_at_digit(formula: str):
    prefix = ""
    number_str = ""
    
    first_digit_index = -1
    for i in range(len(formula)):
        char = formula[i]
        if char.isdigit():
            first_digit_index = i
            break
    
    if first_digit_index == -1:
        return (formula, 1)
    
    prefix = formula[:first_digit_index]
    number_str = formula[first_digit_index:]
    
    try:
        number = int(number_str)
        return (prefix, number)
    except ValueError:
        return (formula, 1)

def split_before_each_uppercase(formula: str):
    if not formula:
        return []

    parts = []
    current_part = ""
    for char in formula:
        if char.isupper():
            if current_part:
                parts.append(current_part)
            current_part = char
        else:
            current_part += char
            
    if current_part:
        parts.append(current_part)
        
    return parts
