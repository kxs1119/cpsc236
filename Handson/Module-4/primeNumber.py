def getValid():
    while True:
        try:
            num = int(input("Please enter an integer between 1 and 5000: "))
            if 1 <= num <= 5000:
                return num
            else:
                print("Invalid integer. Please try again.")
        except ValueError:
            print("Invalid integer. Please try again.")

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def countFactors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count