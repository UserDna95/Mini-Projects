def calculate_total_tax(income):
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

    def calculate_tax(income, brackets):
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
        
    federal_tax = calculate_tax(income, federal_tax_brackets)
    provincial_tax = calculate_tax(income, provincial_tax_brackets)

    return federal_tax, provincial_tax



income = float(input("What is your income: "))
federal_tax, provincial_tax = calculate_total_tax(income)
print(f"Your total federal tax payable is ${federal_tax}")
print(f"Your total provincial tax payable is ${provincial_tax}")