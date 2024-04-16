def get_valid_integer():
    while True:
        try:
            num = int(input("Please enter an integer between 1 and 5000: "))
            if 1 <= num <= 5000:
                return num
            else:
                print("Invalid integer. Please try again.")
        except ValueError:
            print("Invalid integer. Please try again.")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_factors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count