from matrix import *
import random
def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()


###
### initialize variables
###     

#ㅁㅁㅁㅁ
stick = [ [ [ 0 , 0 , 1 ,0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] ],
       [ [ 1 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 0] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] ],
       [ [ 1 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]

#ㅁㅁ
#ㅁㅁ
sq = [ [ [ 1, 1 ], [ 1, 1 ] ],
      [ [ 1, 1 ], [ 1, 1 ] ],
      [ [ 1, 1 ], [ 1, 1 ] ],
      [ [ 1, 1 ], [ 1, 1 ] ] ]

#  ㅁ
#ㅁㅁㅁ
t = [ [ [ 0, 1, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ] ],
      [ [ 0, 1, 0 ], [ 0, 1, 1 ], [ 0, 1, 0 ] ],
      [ [ 0, 0, 0 ], [ 1, 1, 1 ], [ 0, 1, 0 ] ],
      [ [ 0, 1, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ] ] ]

#  ㅁ
#  ㅁ
#ㅁㅁ
j =  [ [ [ 0, 1, 0 ], [ 0, 1, 0 ], [ 1, 1, 0 ] ],
      [ [ 1, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ] ],
      [ [ 0, 1, 1 ], [ 0, 1, 0 ], [ 0, 1, 0 ] ],
      [ [ 0, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 1 ] ]]

#ㅁ
#ㅁ
#ㅁㅁ
L = [ [ [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 1 ] ],
      [ [ 0, 0, 0 ], [ 1, 1, 1 ], [ 1, 0, 0 ] ],
      [ [ 1, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ] ],
      [ [ 0, 0, 1 ], [ 1, 1, 1 ], [ 0, 0, 0 ] ]]

#  ㅁㅁ 
#ㅁㅁ
s = [ [ [ 0, 1, 1 ], [ 1, 1, 0 ], [ 0, 0, 0 ] ],
      [ [ 0, 1, 0 ], [ 0, 1, 1 ], [ 0, 0, 1 ] ],
      [ [ 0, 0, 0 ], [ 0, 1, 1 ], [ 1, 1, 0 ] ],
      [ [ 1, 0, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ] ]]
      
#ㅁㅁ
#  ㅁㅁ
z = [ [ [ 1, 1, 0 ], [ 0, 1, 1 ], [ 0, 0, 0 ] ],
      [ [ 0, 0, 1 ], [ 0, 1, 1 ], [ 0, 1, 0 ] ],
      [ [ 0, 0, 0 ], [ 1, 1, 0 ], [ 0, 1, 1 ] ],
      [ [ 0, 1, 0 ], [ 1, 1, 0 ], [ 1, 0, 0 ] ]]


arrayBlk = [stick, sq, t, j, L, s, z]

### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]


rand = random.randint(0, 6)

idx = 0
###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk[rand][idx])
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###




while True:
    
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        idx = (idx + 1) % 4
        currBlk = Matrix(arrayBlk[rand][idx])

    elif key == ' ': # drop the block
        while not tempBlk.anyGreaterThan(1):
            top += 1
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            idx = (idx - 1) % 4
            currBlk = Matrix(arrayBlk[rand][idx])
        elif key == ' ': # undo: move up
            top -= 1
            newBlockNeeded = True

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False

        rand = random.randint(0, 6)
        idx = 0

        currBlk = Matrix(arrayBlk[rand][idx])
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
