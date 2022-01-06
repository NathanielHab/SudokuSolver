

def formatPrint(S):
    '''prints the sudoku board in a nice, readable format'''
    if len(S) == 0:
        return
    print("-------------------------------------------")
    for r in range(9):
        print("", end='|  ')
        for i in range(9):
            if (i+1)%3 == 0:
                print(str(S[r][i]), end='  |  ')
            else:
                print(str(S[r][i]), end=' | ')
        if r != 8:
            if (r+1)%3 == 0:
                print("\n| ------------+-------------+------------ |")
            else:
                print("\n| ---+---+--- | ---+---+--- | ---+---+--- |")
        else:
            print("\n-------------------------------------------")
    print()


def fits(r, i, n):
    '''returns true if number n is possible in position S[r][i] of sudoku S'''
    global S
    for j in range(9):
        if ((S[r][j] == n) or (S[j][i] == n)):  #check rows and columns
            return False
    x = (i//3)*3
    y = (r//3)*3
    for j in range(3): #check 3x3 boxes
        for k in range(3):
            if S[y+j][x+k] == n:
                return False
    return True  #n is possible
        
        
def solveWell():
    '''solves sudoku S using backtracking'''
    global S
    for r in range(9):
        for i in range(9):
            if S[r][i] == 0:
                for n in range(1,10):
                    if fits(r, i, n):
                        S[r][i] = n
                        solveWell()
                        S[r][i] = 0
                return
    formatPrint(S)
    return


#easy one
S = [[8,1,7,0,0,0,0,4,5],[0,0,0,0,5,1,7,0,6],[2,6,5,0,0,3,0,0,1],[4,7,0,5,6,8,0,0,0],[9,5,1,0,0,0,0,8,0],[0,3,0,0,9,0,2,0,0],[0,4,0,2,0,0,0,0,0],[0,0,0,0,0,5,0,7,9],[5,8,9,7,3,0,1,6,0]]

#hard one (does not work yet)
S = [[5,0,0,0,0,1,0,4,0],[8,0,0,7,4,0,5,0,0],[1,0,0,3,8,0,9,0,0],[0,0,2,0,0,4,0,0,0],[6,0,0,0,3,0,0,0,1],[0,0,0,6,0,0,4,0,0],[0,0,8,0,7,9,0,0,4],[0,0,7,0,2,3,0,0,6],[0,3,0,4,0,0,0,0,2]]

#hard2
S = [[9,0,0,0,6,5,0,2,0],[0,8,7,0,0,0,0,1,0],[0,0,0,0,0,0,0,8,0],[0,7,0,0,0,0,0,0,0],[0,0,2,4,3,0,5,0,0],[0,0,0,0,1,0,7,0,0],[8,9,0,0,0,4,0,0,0],[0,0,6,0,0,0,3,0,0],[0,4,0,0,2,9,0,0,0]]

#hardest one
#S = [[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]

#Ask for input
while True:
    inp = input("Give a sudoku or click enter to use a default sudoku. 'q' to quit: ").split("],[")
    if inp == ['q']:
        break
    try:
        inp[0] = inp[0][2:]
        inp[8] = inp[8][:-2]
        for i in range(9):
            inp[i] = inp[i].split(',')
            for j in range(9):
                inp[i][j] = int(inp[i][j])

        if len(inp) == 9:
            for i in range(9):
                if len(inp[i]) != 9:
                    print("\nBad input. Solving default sudoku...")
                    break
            print("\nSolving input...")
            S = inp
        elif len(inp) != 0:
            print("\nBad input. Solving default sudoku...")
        else:
            print("\nSolving default sudoku...")
    except:
        print("\nBad input. Solving default sudoku...")

    #Run the code
    print("\n               Given sudoku             ")
    formatPrint(S)
    print("\n               Solved sudoku            ")
    solveWell()

print("\nGoodbye!")







    
        
