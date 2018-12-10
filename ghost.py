from random import randint
print('Ghost Game')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 3)
    print('three doors ahead...')
    print('A ghost behind one...')
    print('Which door do you open?')
    door = input('1, 2 or 3 ?')
    door_num = int(door)
    if door_num == ghost_door:
        print('Ghost')
        feeling_brave = False
    else:
        print('No ghost!')
        print('You enter tht next room')
        score = score +1
        print('Run away!')
        print('Game over, scored' + str(score))

from turtle import*
forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)
for i in range(3):
    forward(100)
    right(120)
