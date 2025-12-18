import random

array = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']
         ]
posarr = [1,2,3,4,5,6,7,8,9]

def isfull(arr):
    for row in arr:
        for col in row:
            if col == '_':
                return False
    return True

def is_solved_a(arr):
    for i in range(3):
        if arr[i][0] == arr[i][1] and arr[i][1] == arr[i][2] and arr[i][0] != '_':
            if arr[i][0] == 'X':
                return -1
            else:
                return 1
        if arr[0][i] == arr[1][i] and arr[1][i] == arr[2][i] and arr[0][i] != '_':
            if arr[0][i] == 'X':
                return -1
            else:
                return 1
    if arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2] and arr[0][0] != '_':
        if arr[0][0] == 'X':
            return -1
        else:
            return 1
    if arr[0][2] == arr[1][1] and arr[1][1] == arr[2][0] and arr[2][0] != '_':
        if arr[2][0] == 'X':
            return -1
        else:
            return 1
    if isfull(arr):
        return 0
    return 404
def calc_score(arr, turn):
    if is_solved_a(arr) != 404:
        return is_solved_a(arr)
    if turn == 'O':
        best_score = -2
        for i in range(3):
            for j in range(3):
                if arr[i][j] == '_':
                    arr[i][j] = turn
                    score = calc_score(arr, 'X')
                    arr[i][j] = '_'
                    if score > best_score:
                        best_score = score
        return best_score
    elif turn == 'X':
        best_score = 2
        for i in range(3):
            for j in range(3):
                if arr[i][j] == '_':
                    arr[i][j] = turn
                    score = calc_score(arr, 'O')
                    arr[i][j] = '_'
                    if score < best_score:
                        best_score = score
        return best_score



def best_move(arr):
    pos = 0
    best_score = -2
    for i in range(3):
        for j in range(3):
            if arr[i][j] == '_':
                arr[i][j] = 'O'
                if best_score < calc_score(arr, 'X'):
                    best_score = calc_score(arr, 'X')
                    pos = 3 * i + j
                arr[i][j] = '_'
    return pos+1



def is_solved(arr):
    for i in range(3):
        if arr[i][0] == arr[i][1] and arr[i][1] == arr[i][2] and arr[i][0] != '_':
            print()
            print(arr[i][0],' Won!')
            return True
        if arr[0][i] == arr[1][i] and arr[1][i] == arr[2][i] and arr[0][i] != '_':
            print()
            print(arr[0][i],' Won!')
            return True
    if arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2] and arr[0][0] != '_':
        print()
        print(arr[0][0],' Won!')
        return True
    if arr[0][2] == arr[1][1] and arr[1][1] == arr[2][0] and arr[2][0] != '_':
        print(arr[0][2],' Won!')
        print()
        return True
    if len(posarr) == 0:
        print()
        print('Oops! it\'s a draw!!')
        return True
    return False
def show(arr):
    for i in range(3):
        for j in range(3):
            print(str(arr[i][j]), end='  ')
        print()

def solvetictactoe(arr, level):
    if is_solved(arr):
        return
    pos = int(input('Enter pos(1 - 9): '))
    if (pos<1 or pos>9):
        print('Choose pos between 1 and 9 only')
        solvetictactoe(arr, level)
        return
    try:
        posarr.remove(pos)
    except:
        print('Can\'t place choose other pos')
        solvetictactoe(arr, level)
        return
    arr[(pos-1)//3][(pos-1)%3] = 'X'
    print()
    print('Your Move: ')
    show(arr)
    if is_solved(arr):
        return
    if level == 'easy':
        randpos = random.choice(posarr)
    else:
        randpos = best_move(arr)
    arr[(randpos-1)//3][(randpos-1)%3] = 'O'
    print()
    print('Computer Move: ')
    show(arr)
    posarr.remove(randpos)
    solvetictactoe(arr, level)
show(array)
lvl = input('Choose difficulty (Easy / Hard): ')
if input('Will you make first move (y/n) : ').lower() == 'n':
    if lvl == 'easy':
        randpos = random.choice(posarr)
    else:
        randpos = best_move(array)
    array[(randpos - 1) // 3][(randpos-1) % 3] = 'O'
    print()
    print('Computer Move: ')
    show(array)
    posarr.remove(randpos)
print('You are X.')
solvetictactoe(array, lvl)