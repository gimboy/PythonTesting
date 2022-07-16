# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
findInText="йцу"

def checkSecondEntry(list,findInText):
    k=0
    count=0
    for i in list:
        count+=1
        if(i==findInText and k==1):
            return count
        if i==findInText:
            k+=1
    return -1

print(checkSecondEntry(list,findInText))