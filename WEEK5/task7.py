def calculate_tax(income, /, *, tax_rate=0.1):
    tax = income * tax_rate
    return tax


przychod = 2137.69
podatek = calculate_tax(przychod)
print(f'Podatek od kwoty {przychod} wynosi {podatek:.2f}')
