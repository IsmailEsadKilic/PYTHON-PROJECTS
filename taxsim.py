"""
first 10 000 --> 0%
next 10 000 --> 10%
rest      --> 20%

example tax of 45000 should be 6000
"""
window = 10000
rate1 = 0
rate2 = 1/10
rate3 = 2/10


def tax_calc(income,window,rate1,rate2,rate3):

    if income <= window:
        tax = income * rate1
        return tax
    elif income > window and income <= window * 2:
        tax = (income-window) * rate2 + tax_calc(window,window,rate1,rate2,rate3)
        return tax
    elif income > window * 2:
        tax = (income-window * 2) * rate3 + tax_calc(window * 2,window,rate1,rate2,rate3)
        return tax

print(tax_calc(int(input("input moneh: ")),window,rate1,rate2,rate3))
