#-*- coding:utf-8 -*-
direction = 'E' # E, W, N ,S
positionX = 'E'
positionY = 'N'
positionEastWest = 0
positionNorthSouth = 0

def setChangeDirection (position, number, newPosition):
    if (number < 0):
        position = newPosition
        number = abs (number)

def setForward (position, number):
    if (position == 'E' or position == 'W'):
        positionEastWest += number
    if (position == 'N' or position == 'S'):
        positionNorthSouth += number

def setDirection (newDirection, number):

    if (newDirection == 'W' and number == 90):

        if (position == 'N'):
            position = 'W'

        if (position == 'S'):
            position = 'W'

        if (position == 'E'):
            position == 'S'

        if (position == 'W'):
            position == 'N'

    if (newDirecton == 'L' and number == 90):
       
        if (position == 'N'):
            position = 'E'

        if (position == 'S'):
            positon = 'S'

        if (position == 'E'):
            position = 'N'

        if (position == 'W'):
            position = 'S'
        

    if (position == 'N' and number==180):
        position = 'S'
    if (position == 'S' and number == 180):
        positon = 'N'
    if (position =='W' and number == 180):
        position = 'E'
    if (position =='E' and number == 180):
        postion = 'W'

def main():
    file1 = open ('12.txt','r')
    lines = file1.readlines()

    for line in lines:
        letter = line[0:1]
        number = line[1:]

        if (letter == 'F'):
            setForward (letter, number)
        
        if (letter == 'L' or letter =='W'):
            setDirection (letter, number)


        if (letter == 'N' and position == 'N'):
                positionNorthSouth += number;

        if (letter == 'N' and position == 'S'):
            positionNorthSouth -= number
            if (positionNorthSouth < 0):
                postion = 'N'

        # order is S with number         
        if (letter == 'S' and position == 'S'):
            positionNorthSouth += number; 

        if (letter == 'S' and position== 'N'):
            positonNorthSouth -= number;
            if (positionNorthSouth < 0):
                letter = 'N'
                positionNorthSouth = abs(positionNorthSouth)

        # order is E with number
        if (letter =='E' and position =='E'):
            positionEastWest += number;
        if (letter == 'E' and position == 'W'):
            positionNorthSouth -= number;
            if (positionEastWest < 0):
                letter = 'W'
                positionEastWest = abs(positionEastWest)

        # order is W with number
        if (letter == 'W' and position == 'W'):
            positionEastWest += positionEastWest
        if (letter == 'W' and position == 'E'):
            positionEastWest -= number
            if (positionEastWest < 0):
                letter = 'E'
                positionEastWest = abs(positionEastWest)

            
        print (letter + ' la posicion ahora es ' + number)

    suma = int(positionEastWest) + int (positionEastWest)
   # print (' la posicion E-W: ' + positionEastWest)
   # print (' la posicion N-S: ' + positionNothSouth)
   # print (' la posici�n final: ' + suma) 

if __name__ == "__main__":
    main()


