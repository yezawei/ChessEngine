"""responsible for handing user's input and displaying the current gamestate object"""
import pygame as p
from chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
Initialize a global disctionary of images. This will be called only once in a main. 
"""

def loadImages():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK',
              'bp', 'wB', 'wN', 'wR', 'wQ', 'wK', 'wp']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        # access the image by calling 'IMAGES['wp']

"""
Main driver for user input and updating graphics
"""


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    sqSelected = () #no square is selected initially, keeping track of the last click of the user(tuple(row,col)).
    playerClicks = [] #keeping track of player clicks.
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y) mouse location
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2: #after 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () #reset user clicks
                    playerClicks = []

            #key clicks
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: #z to undo move
                    gs.UndoMove()

            clock.tick(MAX_FPS)
            p.display.flip()
            drawGameState(screen, gs)
'''
Responsive for all the graphics within a current game state.
'''


def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on the board
    drawPieces(screen, gs.board) #draw pieces on the board

def drawBoard(screen):
    colors = [p.Color("light gray"), p.Color("dark green")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #not empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))




if __name__ == '__main__':
    main()