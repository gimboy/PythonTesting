x = int(input('x= '))
y = int(input('y= '))

def сoordinatePlaneNumber(x,y):
    if x>0 and y>0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    elif x>0 and y<0:
        return 4
    else:
        return 'dont write 0'
print(сoordinatePlaneNumber(x,y))