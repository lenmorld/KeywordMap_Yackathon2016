print ("Hello World")

def checkIfPrime (num) :
    for x in range (2, num):
        if (num % x == 0):
            return False
    return True

answer = checkIfPrime(15)

print(answer)
