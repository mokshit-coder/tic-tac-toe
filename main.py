import random

array = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']
         ]
posarr = [1,2,3,4,5,6,7,8,9]
def is_solved(arr):
    for i in range(3):
        if arr[i][0] == arr[i][1] and arr[i][1] == arr[i][2] and arr[i][0] != '_':
            print(arr[i][0],' Won!')
            return True
        if arr[0][i] == arr[1][i] and arr[1][i] == arr[2][i] and arr[0][i] != '_':
            print(arr[0][i],' Won!')
            return True
    if arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2] and arr[0][0] != '_':
        print(arr[0][0],' Won!')
        return True
    if arr[0][2] == arr[1][1] and arr[1][1] == arr[2][0] and arr[2][0] != '_':
        print(arr[0][2],' Won!')
        return True
    if len(posarr) == 0:
        print('Oops! it\'s a draw!!')
        return True
    return False
def show(arr):
    for i in range(3):
        for j in range(3):
            print(str(arr[i][j]), end='  ')
        print()

def solvetictactoe(arr):
    if is_solved(arr):
        return
    pos = int(input('Enter pos(1 - 9): '))
    if (pos<1 or pos>9):
        print('Choose pos between 1 and 9 only')
        solvetictactoe(arr)
        return
    try:
        posarr.remove(pos)
    except:
        print('Can\'t place choose other pos')
        solvetictactoe(arr)
        return
    arr[(pos-1)//3][pos%3 - 1] = 'X'
    print()
    print('Your Move: ')
    show(arr)
    if is_solved(arr):
        return
    randpos = random.choice(posarr)
    arr[(randpos-1)//3][randpos%3 - 1] = 'O'
    print()
    print('Computer Move: ')
    show(arr)
    posarr.remove(randpos)
    solvetictactoe(arr)
show(array)
if input('Will you make first move (y/n) : ').lower() == 'n':
    randpos = random.choice(posarr)
    array[(randpos - 1) // 3][randpos % 3 - 1] = 'O'
    print()
    print('Computer Move: ')
    show(array)
    posarr.remove(randpos)
print('You are X.')
solvetictactoe(array)

