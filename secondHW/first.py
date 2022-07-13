x = float(input('Введите вещественное число'))

def showSumNumber(x):
    sum = 0
    x=str(x)
    x=x.replace(".","")
    length=len(x)
    for i in x:
        i=int(i)
        sum+=i%10
    return sum   
print(showSumNumber(x))