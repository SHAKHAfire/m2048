import random as rand
from tabulate import tabulate as tab
COLUMNS=4
ROWS=4

matrix=[[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

# temporary
# matrix=[[0,2,0,0],
#         [0,2,0,0],
#         [0,64,2,2],
#         [2,2,0,2],]



def display () -> None:

    to_tab=[]
    for i in matrix:
        if 1:
            to_tab.append(i)
    for ind,i in enumerate(to_tab):
        for horind,num in enumerate(i):
            if to_tab[ind][horind]==0:
                to_tab[ind][horind]=' '


    to_print=tab(to_tab, tablefmt='rounded_grid',colalign=['center']*ROWS,)

    for ind,i in enumerate(to_tab):
        for horind,num in enumerate(i):
            if to_tab[ind][horind]==' ':
                to_tab[ind][horind]=0
    # for i in matrix:
    #     to_print+='\n'

    #     for num in i:
    #         to_print+=f'{" "*(biggest-len(str(num)))+str(num) if num else " "*biggest}|'
        
    print(to_print)




def any_space() -> bool:
    for i in matrix:
        if 0 in i:
            return True
    return False

def spawn():
    row =rand.randrange(ROWS)
    column=rand.randrange(COLUMNS)
    if not matrix[row][column]:
        matrix[row][column] = 4 if rand.randrange(10) == 1 else 2
    elif any_space():
        spawn()
    else:print('you lost')


def vert_move(direction:['up','down']):
    if direction == 'down':
        matrix.reverse()
    def push_up():
        for i in range(COLUMNS-1):
            for ind,i in enumerate(matrix):
                
                for horind,num in enumerate(i):
                    if num ==0 and ind != COLUMNS-1:
                        matrix[ind][horind]=matrix[ind+1][horind]
                        matrix[ind+1][horind]=0
    push_up()
    # merging
    for ind,i in enumerate(matrix):
        if ind !=0:
            for horind,num in enumerate(i):
                if matrix[ind-1][horind]==num and num!=0:
                    matrix[ind][horind]=0
                    matrix[ind-1][horind]*=2
    push_up()
    if direction == 'down':
        matrix.reverse()

def horison_move(direction:['left','right']):
    if direction =='right':
        for ind,i in enumerate( matrix):
            matrix[ind].reverse()

    def push_side():
        for _ in range(ROWS-1):
            for ind,hor in enumerate(matrix):
                for horind,num in enumerate(hor):
                    if horind !=0:
                        if num != 0 and matrix[ind][horind-1]==0:
                            matrix[ind][horind]=0
                            matrix[ind][horind-1]=num
    push_side()    

    for ind,hor in enumerate(matrix):
        for horind,num in enumerate(hor):
            if horind !=0:
                if num != 0 and matrix[ind][horind-1]==num:
                    matrix[ind][horind]=0
                    matrix[ind][horind-1]*=2
    push_side()

    if direction =='right':
        for ind,i in enumerate( matrix):
            matrix[ind].reverse()






def main():
    spawn()
    display()
    while True:
        action=input('enter the action (WSAD)(EX to exit)\n>>>')
        if action.lower() =='w':
            vert_move('up')
            spawn()

        elif action.lower() =='s':
            vert_move('down')
            spawn()

        elif action.lower()=='a':
            horison_move('left')
            spawn()

        elif action.lower()=='d':
            horison_move('right')
            spawn()

        elif action.lower()=='ex':
            break
        else:print('[INFO] you should enter one of (W,A,S,D,EX) in any case')
            
        display()


if __name__ =="__main__":
    main()

