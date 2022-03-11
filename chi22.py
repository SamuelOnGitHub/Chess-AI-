import random, copy, pygame, sys, math, time
from pygame.locals import *
pygame.init()

GREY = pygame.Color(128, 128, 128)   # Grey
RED = pygame.Color(255, 0, 0)       # Red
WINDOW = pygame.display.set_mode((800,800))
bcastle = pygame.image.load("blackcastle.png")
bknight = pygame.image.load("blackknight.png")
bbishop = pygame.image.load("blackbishop.png")
bqueen = pygame.image.load("blackqueen.png")
bking = pygame.image.load("blackking.png")
bpawn = pygame.image.load("blackpawn.png")

wcastle = pygame.image.load("whitecastle.png")
wknight = pygame.image.load("whitehorse.png")
wbishop = pygame.image.load("whitebishop.png")
wqueen = pygame.image.load("whitequeen.png")
wking = pygame.image.load("whiteking.png")
wpawn = pygame.image.load("whitepawn.png")


global_chessboard = [   [" ","  ","  ","  ","  ","  ","  ","  ","  "," "],
                        [" ","rc","rr","rb","rq","rk","rb","rr","rc"," "],
                        [" ","rmp","rmp","rmp","rmp","rmp","rmp","rmp","rmp"," "],
                        [" ","oo","oo","oo","oo","oo","oo","oo","oo"," "],
                        [" ","oo","oo","oo","oo","oo","oo","oo","oo"," "],
                        [" ","oo","oo","oo","oo","oo","oo","oo","oo"," "],
                        [" ","oo","oo","oo","oo","oo","oo","oo","oo"," "],
                        [" ","hmp","hmp","hmp","hmp","hmp","hmp","hmp","hmp"," "],
                        [" ","hc","hr","hb","hq","hk","hb","hr","hc"," "],
                        [" ","  ","  ","  ","  ","  ","  ","  ","  "," "] ]

global_humanPiecePositions = [(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8)]
global_robotPiecePositions = [(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8)]

global_moves = {
    "o" : [(20,20)],
    "c" : [(-8,0),(-7,0),(-6,0),(-5,0),(-4,0),(-3,0),(-2,0),(-1,0),(8,0),(7,0),(6,0),(5,0),(4,0),(3,0),(2,0),(1,0),(0,-8),(0,-7),(0,-6),(0,-5),(0,-4),(0,-3),(0,-2),(0,-1),(0,8),(0,7),(0,6),(0,5),(0,4),(0,3),(0,3),(0,2),(0,1)],
    "r" : [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)],
    "b" : [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),(-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),(1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
    "q" : [(-8, 0), (-7, 0), (-6, 0), (-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, -8), (0, -7), (0, -6), (0, -5), (0, -4), (0, -3), (0, -2), (0, -1), (0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (0, 3), (0, 2), (0, 1), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7), (-8, -8), (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7), (-8, 8), (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7), (8, -8)],
    "k" : [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)],
    "p" : [(1,0),(1,1),(1,-1),(-1,0),(-1,-1),(-1,1),(2,0),(-2,0)]
}

global_pieceScores= {
    "c":3,
    "r":2,
    "b":3,
    "q":4,
    "k":100,
    "p":1
}

def drawBoard(board):
    WINDOW.fill(GREY)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(WINDOW, RED, (i * 100, j * 100, 100, 100))
                
    for a in range(8):
        for b in range(8):
            if board[a + 1][b + 1] != "oo" and board[a + 1][b + 1] != " ":
                if board[a + 1][b + 1] == "rc":
                    WINDOW.blit(bcastle, (b * 100, a * 100))
                if board[a + 1][b + 1] == "rr":
                    WINDOW.blit(bknight, (b * 100, a * 100))
                if board[a + 1][b + 1] == "rb":
                    WINDOW.blit(bbishop, (b * 100, a * 100))
                if board[a + 1][b + 1] == "rq":
                    WINDOW.blit(bqueen, (b * 100, a * 100))
                if board[a + 1][b + 1] == "rk":
                    WINDOW.blit(bking, (b * 100, a * 100))
                if board[a + 1][b + 1] == "rp" or board[a + 1][b + 1] == "rmp":
                    WINDOW.blit(bpawn, (b * 100, a * 100))
                if board[a + 1][b + 1] == "hc":
                    WINDOW.blit(wcastle, (b * 100, a * 100))
                if board[a + 1][b + 1] == "hr":
                    WINDOW.blit(wknight, (b * 100, a * 100))
                if board[a + 1][b + 1] == "hb":
                    WINDOW.blit(wbishop, (b * 100, a * 100))
                if board[a + 1][b + 1] == "hq":
                    WINDOW.blit(wqueen, (b * 100, a * 100))
                if board[a + 1][b + 1] == "hk":
                    WINDOW.blit(wking, (b * 100, a * 100))
                if board[a + 1][b + 1] == "hp" or board[a + 1][b + 1] == "hmp":
                    WINDOW.blit(wpawn, (b * 100, a * 100))

    pygame.display.update()

def makeMove(board_input, pos_input, move_input, humanPieceList_input, robotPieceList_input):

    board = copy.deepcopy(board_input)
    
    rowPos = pos_input[0]
    columnPos = pos_input[1]
    rowMove = move_input[0]
    columnMove = move_input[1]
    
    humanPlaying = 0 

    if board[rowPos][columnPos][0] == "h":
        friendlyPieceList = copy.copy(humanPieceList_input)
        enemyPieceList = copy.copy(robotPieceList_input)
        humanPlaying = 1
    elif board[rowPos][columnPos][0] == "r":
        friendlyPieceList = copy.copy(robotPieceList_input)
        enemyPieceList = copy.copy(humanPieceList_input)
    
    if (rowPos + rowMove, columnPos + columnMove) in enemyPieceList:
        enemyPieceList.remove((rowPos + rowMove, columnPos + columnMove)) 
    
    if board[rowPos][columnPos][1] == "m":
        board[rowPos + rowMove][columnPos + columnMove] = board[rowPos][columnPos][0] + board[rowPos][columnPos][-1]
    else:
        board[rowPos + rowMove][columnPos + columnMove] = board[rowPos][columnPos]
    board[rowPos][columnPos] = "oo"
    friendlyPieceList.remove((rowPos, columnPos))
    friendlyPieceList.append((rowPos + rowMove, columnPos + columnMove))

    if humanPlaying == 1:
        return board, friendlyPieceList, enemyPieceList
    else:
        return board, enemyPieceList, friendlyPieceList

def isValidMove(board,pos_input,move_input):

    rowPos = pos_input[0]
    columnPos = pos_input[1]
    rowMove = move_input[0]
    columnMove = move_input[1]
    
    def unit(number):
        if number == 0:
            return 0
        else:
            return int(number / abs(number))

    directions = {"r":1,"h":-1}
    teams = " hr"

    if max(rowPos + rowMove, columnPos + columnMove) <= 8 and min(rowPos + rowMove, columnPos + columnMove) >= 1:
        if board[rowPos][columnPos][-1] == "p":
            if (rowMove) * directions[board[rowPos][columnPos][0]] > 0:
                if abs(rowMove) == 2:
                    if board[rowPos][columnPos][1] == "m" and board[rowPos + rowMove][columnPos + columnMove][0] == "o":
                        return True
                    else:
                        return False
                if (columnMove != 0 and board[rowPos + rowMove][columnPos + columnMove][0] == teams[directions[board[rowPos][columnPos][0]]]) or (columnMove == 0 and board[rowPos + rowMove][columnPos + columnMove][0] == "o"):
                    return True            
        elif board[rowPos + rowMove][columnPos + columnMove] == "o" or board[rowPos][columnPos][0] != board[rowPos + rowMove][columnPos + columnMove][0]:
            for i in range(1, max(abs(rowMove),abs(columnMove))):
                if board[rowPos + (i * unit(rowMove))][columnPos + (i * unit(columnMove))][0] != "o"  and board[rowPos][columnPos][-1] != "r":
                    return False
            return True
    else:
        return False

def evalBoard(board):
    score = 0
    for i in board:
        for j in i:
            if j[0] == "r":
                score += global_pieceScores[j[-1]]
            elif j[0] == "h":
                score -= global_pieceScores[j[-1]]
    return score

def getFutureBoardPositions(CurrentBoardPositions, depth):
    if depth > 0:
        afterHMoves = []
        for position in CurrentBoardPositions:
            board = position[0]
            hPieces = position[1]
            rPieces = position[2]

            for hPiece in hPieces:
                for hMove in global_moves[board[hPiece[0]][hPiece[1]][-1]]:
                    if isValidMove(board, hPiece, hMove):
                        afterHMove = makeMove(board, hPiece, hMove, hPieces, rPieces)
                        afterHMoves.append([afterHMove[0], afterHMove[1], afterHMove[2]])
        
        afterRMoves = []
        for position in afterHMoves:
            board = position[0]
            hPieces = position[1]
            rPieces = position[2]

            bestBoard = 0
            for rPiece in rPieces:
                for rMove in global_moves[board[rPiece[0]][rPiece[1]][-1]]:
                    if isValidMove(board, rPiece, rMove):
                        afterRMove = makeMove(board, rPiece, rMove, hPieces, rPieces)
                        if evalBoard(afterRMove) >= bestBoard:
                            bestBoard = evalBoard(afterRMove)
                            afterRMoves.append([afterRMove[0], afterRMove[1], afterRMove[2]])
                        
        return getFutureBoardPositions(afterRMoves, depth - 1)
    else:
        return CurrentBoardPositions

def gameEnded(board):
    robotkings = 0
    humankings = 0
    for i in board:
        for j in i:
            if j == "rk":
                robotkings += 1
            if j == "hk":
                humankings += 1
    if min(humankings,robotkings) == 0:
        print("ended")
        return True
    else:
        return False

firstMove = True
while not gameEnded(global_chessboard):
    drawBoard(global_chessboard)
    
    print("Human To Play\n")
    moved = False
    while not moved:
        startCoord = ()
        moveVect = ()
        while startCoord == () or moveVect == ():
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    startCoord = (math.floor(y/100) + 1, math.floor(x/100) + 1)
                if event.type == pygame.MOUSEBUTTONUP and startCoord != ():
                    x, y = pygame.mouse.get_pos()
                    endCoord = (math.floor(y/100) + 1, math.floor(x/100) + 1)
                    moveVect = (endCoord[0] - startCoord[0], endCoord[1] - startCoord[1])
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        if isValidMove(global_chessboard, startCoord, moveVect) and moveVect in global_moves[global_chessboard[startCoord[0]][startCoord[1]][-1]]:
            moveMade = makeMove(global_chessboard, startCoord, moveVect, global_humanPiecePositions, global_robotPiecePositions)
            global_chessboard = moveMade[0]
            global_humanPiecePositions = moveMade[1]
            global_robotPiecePositions = moveMade[2]
            moved = True
        else:
            print(startCoord, moveVect, " Invalid Move")
    
    drawBoard(global_chessboard)

    print("Robot To Play")
    
    if firstMove:
        #openingPiece = random.choice([(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(1,2),(1,7)])
        #openingMove = random.choice(global_moves[global_chessboard[openingPiece[0]][openingPiece[1]][-1]])
        openingPiece = (2,5)
        openingMove = (2,0)
        while not isValidMove(global_chessboard, openingPiece, openingMove):
            openingMove = random.choice(global_moves[global_chessboard[openingPiece[0]][openingPiece[1]][-1]])
        movemade = makeMove(global_chessboard, openingPiece, openingMove, global_humanPiecePositions, global_robotPiecePositions)
        global_chessboard = movemade[0]
        global_humanPiecePositions = movemade[1]
        global_robotPiecePositions = movemade[2]
        firstMove = False
    else:   
        maxscore = -1000000000000000000000
        bestmoves = [[(2,1),(1,0)]]
        boardSum = 0
        for piece in global_robotPiecePositions:
            for move in global_moves[global_chessboard[piece[0]][piece[1]][-1]]:
                if isValidMove(global_chessboard, piece, move):
                    movescore = 0
                    afterMove = makeMove(global_chessboard, piece, move, global_humanPiecePositions, global_robotPiecePositions)
                    futureBoards = getFutureBoardPositions([ [afterMove[0], afterMove[1], afterMove[2]] ], 2)
                    boardSum += len(futureBoards)
                    for board in futureBoards:
                        movescore += evalBoard(board[0])
                    if movescore > maxscore:
                        maxscore = movescore
                        bestmoves = [[piece, move]]
                    elif movescore == maxscore:
                        bestmoves.append([piece,move])
        print(boardSum)
        robotMove = random.choice(bestmoves)
        movemade = makeMove(global_chessboard, robotMove[0], robotMove[1], global_humanPiecePositions, global_robotPiecePositions)
        global_chessboard = movemade[0]
        global_humanPiecePositions = movemade[1]
        global_robotPiecePositions = movemade[2] 
drawBoard(global_chessboard)

time.sleep(4)  
pygame.quit()
sys.exit()
    
