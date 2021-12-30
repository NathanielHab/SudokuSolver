import numpy as np


def inRow(n, r):  #n between 1-9
    '''returns true if n is in row r'''
    for i in r:
        if n == i:
            return True
    else:
        return False

def Col(num, S):  #num between 1-9
    '''returns column "num" as a list. S is the sudoku board'''
    ans = []
    for r in S:
        ans.append(r[num-1])
    return ans

def inCol(n, c):  #n between 1-9
    '''returns true if n is in column r'''
    for i in c:
        if n == i:
            return True
    else:
        return False

def Box(num, S):  #num between 1-9
    '''returns box "num" as a list. S is the sudoku board'''
    
    if num < 4:
        p = [S[0], S[1], S[2]]
    elif num < 7:
        p = [S[3], S[4], S[5]]
    else:
        p = [S[6], S[7], S[8]]
        
    if num % 3 == 1:
        q = 0
    elif num % 3 == 2:
        q = 3
    else:
        q = 6
    
    ans = [p[0][q], p[0][q+1], p[0][q+2], p[1][q], p[1][q+1], p[1][q+2], p[2][q], p[2][q+1], p[2][q+2]]
    return ans

def whichBox(r, i):
    if r < 3:
        if i < 3:
            return 1
        elif i < 6:
            return 2
        else:
            return 3
    elif r < 6:
        if i < 3:
            return 4
        elif i < 6:
            return 5
        else:
            return 6
    else:
        if i < 3:
            return 7
        elif i < 6:
            return 8
        else:
            return 9

def isDone(S):
    '''returns true if sudoku S is complete'''
    for r in S:
        for i in r:
            if i == 0:
                return False
    return True

def isStuck(S):
    '''returns true if sudoku S is stuck (no obvious moves)'''
    if isDone(S):
        return False
    t = 0
    while (t < 81):  #try t amount of times to see if we're stuck
        r = 0
        while r < 9:
            i = 0
            while i < 9:
                if S[r][i] == 0:
                    n = 1
                    ans = []
                    while n < 10:
                        if not (inRow(n, S[r]) or inCol(n, Col(i+1, S)) or inRow(n, Box(whichBox(r, i), S))):
                            ans.append(n)  #potential nums in this square
                        n+=1
                    if len(ans) == 1:
                        return False  #we are not stuck
                i+=1
            r+=1
        return True  #we are stuck

def isImpossible(S, maybes):
    '''returns true if sudoku S cannot be completed'''
    #print("checking impossible")
    r = 0
    while r < 9:
        i = 0
        while i < 9:
            if len(maybes[r][i]) == 0:
                return True
            i+=1
        r+=1
    return False

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

##def removeMaybesRow(n, m, r, i, j, maybes):
##    '''removes n and m from maybe list of items in row r other than indices i and j'''
##    for l in range(len(maybes[r])):
##        #print("l: "+ str(l))
##        for e in range(len(maybes[r][l])):
##            #print("e: "+ str(e)+" "+ str(len(maybes[r][l])))
##            if e == len(maybes[r][l]):
##                continue
##            if (maybes[r][l][e] == n or maybes[r][l][e] == m) and (l != i and l != j):
##                maybes[r][l].remove(maybes[r][l][e])
##    return maybes
##
###def guess(S, maybes):
##    
##    
##
##def solve(S, maybes):
##    lastS = []
##    while ((not isDone(S))):# and (not isStuck(S))):
##        r = 0
##        lastS = S.copy()
##        while r < 9:
##            i = 0
##            while i < 9:
##                if (S[r][i] == 0 and len(maybes[r][i]) == 1):
##                    S[r][i] = maybes[r][i][0]
##                if S[r][i] == 0:
##                    n = 1
##                    ans = []
##                    while n < 10:
##                        if not (inRow(n, S[r]) or inCol(n, Col(i+1, S)) or inRow(n, Box(whichBox(r, i), S))):
##                            ans.append(n)  #potential nums in this square
##                            #print(str(ans))
##                        n+=1
##                        #print(str(r+1) +" "+ str(i+1) +" "+ str(n-1))
##                    maybes[r][i] = ans
##                    #print(str(maybes))
##                    if len(ans) == 1:
##                        #print(str(ans))
##                        S[r][i] = ans[0]
##                        #print(str(r+1) +" "+ str(i+1) +" "+ str(n-1) +" "+ str(S))
####                    if len(ans) == 2:
####                        j = 0
####                        while j < 9:
####                            if maybes[r][j] == ans and i != j:
####                                maybes = removeMaybesRow(ans[0], ans[1], r, i, j, maybes)
####                            j+=1
##                if S[r][i] != 0:
##                    maybes[r][i] = [S[r][i]]
##                i+=1
##            r+=1
##        if isStuck(S):
##            break
##    if isImpossible(S, maybes):
##        print("impossible")
##        return []  #indicates S is impossible
##    if isStuck(S): #no progress, so make a guess and check if correct
##        print("gonna guess")
##        r = 0
##        while r < 9:
##            i = 0
##            while i < 9:
##                if len(maybes[r][i]) == 2: #find first square in S that has only 2 possible inputs
##                    print("found potential square (2)")
##                    mG1 = maybes.copy()
##                    mG2 = maybes.copy()
##                    mG1[r][i] = [mG1[r][i][0]]
##                    sG1 = solve(S, mG1)  #guess one
##                    if len(sG1) != 0:
##                        return solve(sG1, mG1)
##                    mG2[r][i] = [mG2[r][i].pop()]
##                    sG2 = solve(S, mG2)  #guess two
##                    if len(sG2) != 0:
##                        return solve(sG2, mG2)
##                i+=1
##            while i < 9:
##                if len(maybes[r][i]) == 3: #find first square in S that has only 3 possible inputs (if none with 2)
##                    print("found potential square (3)")
##                    mG1 = maybes.copy()
##                    mG2 = maybes.copy()
##                    mG3 = maybes.copy()
##                    mG1[r][i] = [mG1[r][i][0]]
##                    sG1 = solve(S, mG1)  #guess one
##                    if len(sG1) != 0:
##                        return solve(sG1, mG1)
##                    mG2[r][i] = [mG2[r][i][1]]
##                    sG2 = solve(S, mG2)  #guess two
##                    if len(sG2) != 0:
##                        return solve(sG2, mG2)
##                    mG3[r][i] = [mG3[r][i].pop()]
##                    sG3 = solve(S, mG3)  #guess three
##                    if len(sG3) != 0:
##                        return solve(sG3, mG3)
##                i+=1
##            r+=1
##        #print(maybes)
##        #formatPrint(S)
##        #solve(S, maybes)
##    if (not isDone(S)):
##        print("not done")
##        solve(S, maybes)
##    print("end")
##    formatPrint(S)
##    return S
##    #formatPrint(S)

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

#initialise list of possible numbers in each square
maybes = [[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]]]

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







    
        
