import sys
import re
from fractions import Fraction


file_path1 = sys.argv[1]
file_path2 = sys.argv[2]

def readFile1(file_path1):

    with open(file_path1) as file:
        content = file.read()
        content = re.split('\n| ',content)
        cX, cY, R = content[0], content[1], content[2]
        cX, cY, R = Fraction(cX),Fraction(cY),Fraction(R)
    return cX, cY, R

def readFile2(file_path2):

    with open(file_path2) as file:
        content = file.read()
        content = content.split('\n')
        dots = []
        count = 0
        for dot in content:
            count+=1
            if count <=100:
                dot.strip()
                dotX,dotY = map(Fraction, dot.split())
                dots.append((dotX,dotY))
            else:
                print('Слишком много точек')
                sys.exit(0)
        return dots

def isInside(cX, cY, R, dotX,dotY):

    hypotenuse = (dotX-cX)*(dotX-cX)+(dotY-cY)*(dotY-cY)
    if hypotenuse < R*R:
        return 1 # Точка принадлежит окружности
    elif hypotenuse == R*R:
        return 0 # Точка лежит НА окружности
    else:
        return 2 # Точка НЕ принадлежит окружности

def main():
    cX,cY,R = readFile1(file_path1)
    dots = readFile2(file_path2)
    for dot in dots:
        dotX,dotY = dot
        print(isInside(cX,cY,R,dotX,dotY))
        

main()