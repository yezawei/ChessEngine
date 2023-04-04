"""storing all the info about current state of the chess game, responsible
for determining the valid moves at the current state, keeps a move log"""


class GameState():
    def __init__(self):
        #board is an 8x8 list, each element of the list has 2 characters.
        #The first character represents colour of the piece, "b" or "w" for black and white.
        #The second character represent the type of the piece.
        #Note: "N" stands for knight.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []



