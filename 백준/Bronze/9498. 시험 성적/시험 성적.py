def Grade(point):
    if point > 100:
        return 'F'
    elif point >= 90:
        return 'A'
    elif point >= 80:
        return 'B'
    elif point >= 70:
        return 'C'
    elif point >= 60:
        return 'D'
    else:
        return 'F'
    

point = int(input())

print(Grade(point))