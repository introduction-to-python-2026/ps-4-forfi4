def split_at_first_digit(formula):
   for i in formule:
       
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
