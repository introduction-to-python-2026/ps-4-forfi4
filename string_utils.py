def split_at_digit(formula: str) -> tuple[str, int]:
    first_digit_index = -1
    
    for i, char in enumerate(formula):
        if char.isdigit():
            first_digit_index = i
            break
            
    if first_digit_index == -1:
        return formula, 1
        
    else:
        prefix = formula[:first_digit_index]
        
        number_str = formula[first_digit_index:]
        
        number = int(number_str)
        
        return prefix, number


def split_before_each_uppercase(formula: str) -> list[str]:
    if not formula:
        return []

    result = []
    current_element = ""

    for char in formula:
        if char.isupper():
          
            if current_element:
                result.append(current_element)
            
            current_element = char
        else:
            current_element += char
            
    if current_element:
        result.append(current_element)
        
    return result

