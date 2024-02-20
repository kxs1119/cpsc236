

def feetToMeters():
    
    number = int(input("Enter feet"))
    feet = round(number / 0.3048,2)
    print(str(feet), "meters") 
    
def metersToFeet():
    
    number = int(input("Enter meters"))
    meters = round(number * 0.3048,2)
    print(str(meters), "feet") 
    