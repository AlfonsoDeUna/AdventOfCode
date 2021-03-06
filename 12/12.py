#-*- coding:utf-8 -*-
from math import fabs, pi
from cmath import rect, phase

with open ("12.txt") as f:
    instructions = list(map((lambda x:[x[0], int(x[1:])]),
        list (filter((lambda x: x!=''),
            map (str.rstrip, f.readlines())))))

def distanciamanh (pos):
    return fabs(pos.real) + fabs(pos.imag)

def calc(instructions):
    # la posici�n es un un n�mero complejo N/S es imaginario y E/W real
    position = complex(0,0)
    direction = complex (1,0)
    
    for i in instructions:
        if i[0] == "N":
            position += complex (0, i[1])
        elif i[0] == "S":
            position += complex (0, -i[1])
        elif i[0] == "E":
            position += complex(i[1],0)
        elif i[0] == "W":
            position += complex(-i[1],0)
        elif i[0] == "L":
            direction = rect (abs(direction), phase(direction) + i[1] / 180 * pi)
        elif i[0] == "R":
            direction = rect (abs(direction), phase(direction) - i[1] / 180 * pi)
        elif i[0] == "F":
            position = position + i[1] * direction
        else:
            exit (1)
    print ("position: ", position)
    print ("direction: " , direction)
    print ("distancia y resultado final", distanciamanh(position))


def main():
    calc (instructions)


if __name__ == "__main__":
    main()
