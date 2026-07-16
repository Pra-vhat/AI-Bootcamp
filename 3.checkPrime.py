'''
Check if a number is prime
'''


def checkPrime(num):
    count = 0
    if(num == 0 or num == 1):
        return f"{num} is not Prime"
    for i in range(2, num):
        if num % i == 0:
            return f"{num} is not Prime"
        
    return f"{num} is Prime"


for i in range(11):
    print(checkPrime(i))