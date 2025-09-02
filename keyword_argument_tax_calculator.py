def calculate_total_tax(income, level='f'):
    if not isinstance(income, (int, float)) or income < 0:
        return None
    
    federal_tax_brackets = [
        (57375, 0.15),
        (114750, 0.205),
        (177882, 0.26),
        (253414, 0.29), 
        (float('inf'), 0.33)
    ]

    provincial_tax_brackets = [
        (52886, 0.05),
        (105775, 0.09),
        (150000, 0.11),
        (220000, 0.12), 
        (float('inf'), 0.13)
    ]

    brackets = federal_tax_brackets if level.lower() == 'f' else provincial_tax_brackets
    tax = 0 
    lower = 0
    for upper, rate in brackets:
            if income > lower:
                taxable = min(income, upper) - lower
                tax += taxable * rate
                lower = upper
            else:
                break
    return round(tax, 2)

print(calculate_total_tax(55000, 'f'))
print(calculate_total_tax(55000, 'p'))