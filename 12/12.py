direction = 'E' # E, W, N ,S
positionX = 'E'
positionY = 'N'
positionEastWest = 0
positionNorthSouth = 0

def setChangeDirection (position, number, newPosition):
    if (number < 0):
        position = newPosition
        number = abs (number)

def setForward (position, number)
    if (position == 'E' or position == 'W'):
        positionEastWest += number
    if (position == 'N' or position == 'S'):
        positionNorthSouth += number

def setDirection (newDirection, number)

    if (newDirection == 'W'):

        if (position == 'N' and number ==90):
            position = 'W'

        if (position == 'N' and number==180):
            position = 'S'

        if (position == 'S' and number == 90):
            position = 'W'

        if (position == 'S' and number==180):
            position == 'N'

        if (position == 'E' and number==90):
            position == 'S'

        if (position == 'E' and number==180):
            position == 'W'
    
        if (position == 'W' and number==90):
            position == 'N'

        if (position == 'W' and number==180):
            position == 'E'

def main():
    print ("hello")
    file1 = open ('12.txt','r')
    lines = file1.readlines()

    for line in lines:
        letter = line[0:1]
        number = line[1:]

        if (letter == 'F'):
            setForward (position, number)
        
        if (letter == 'L' or letter =='W')


        if (letter == 'N' and position='N'):
                positionNorthSouth += number;

        if (letter == 'N' and position='S'):
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
        if (letter =='E' && position =='E'):
            positionEastWest += number;
        if (letter == 'E' && position == 'W'):
            positionNorthSouth -= number;
            if (positionEastWest < 0):
                letter = 'W'
                positionEastWest = abs(positionEastWest)

        # order is W with number
        if (letter == 'W' && position == 'W'):
            positionEastWest += positionEastWest
        if (letter == 'W' && position == 'E'):
            positionEastWest -= number
            if (positionEastWest < 0):
                letter = 'E'
                positionEastWest = abs(positionEastWest)

            
        print (letter + ' la posicion ahora es ' + number);

if __name__ == "__main__":
    main()


