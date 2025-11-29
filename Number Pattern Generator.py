def number_pattern(n):
    # Check if argument is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    # Check if argument is greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    # Use a for loop to generate the number pattern
    result = []
    for i in range(1, n + 1):
        result.append(str(i))
    
    return " ".join(result)