''' 
This file will be used to make modules for conversions  
'''

def salesTax(number):
    basePrice = number 
    salesTax = number * 0.6
    return salesTax

def afterTax(number,salesTax):
    
    basePrice = number 
    totalTax = basePrice + salesTax
    return  totalTax 
