#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет
a = int(input()) 

def checkDayOfWeek(a):
    if a==1 or a==2 or a==3 or a==4 or a ==5 or a==6: 
     return 'no'
    elif a==6 or a==7: 
     return 'yes'
    else:
     return 'its not number 1..7'

print(checkDayOfWeek(a))