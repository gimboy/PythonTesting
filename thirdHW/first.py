# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
from operator import truediv


list = ['re','af','fa','af','af','af','af']

def checkDigit(list):
    for i in list:
        if type(i)==int:
            return True
        else:
            return False

print(checkDigit(list))