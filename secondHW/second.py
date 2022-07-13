x = int(input('Введи число N '))

def setOfNumbers(x):
    ar = []
    for i in range(1,x+1):
        ar.append(fact(i))
    return ar



def fact(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

print(setOfNumbers(x))