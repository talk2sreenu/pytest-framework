def number_pattern(n):
    num_pattern = ''
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    for num in range(n):
        num_pattern += str(num+1) + ' '
    print(num_pattern)
    return num_pattern.strip()

number_pattern(4)

