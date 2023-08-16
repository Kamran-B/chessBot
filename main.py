from time import sleep
import random
import chess
import TreeNode


def evaluate(board):
    checkBonus = 3
    whiteScore = 0
    blackScore = 0
    for (piece, value) in [(chess.PAWN, 1), (chess.KNIGHT, 3), (chess.BISHOP, 3), (chess.ROOK, 5), (chess.QUEEN, 9)]:
        whiteScore += len(board.pieces(piece, chess.WHITE)) * value
        blackScore += len(board.pieces(piece, chess.BLACK)) * value

    if board.is_check():
        if board.turn: # White's turn
            whiteScore -= checkBonus
            blackScore += checkBonus
        else: # Black's turn
            whiteScore += checkBonus
            blackScore -= checkBonus

    if board.is_checkmate():
        if board.turn: # White's turn
            whiteScore = 0
            blackScore = 1000000
        else: # Black's turn
            whiteScore = 1000000
            blackScore = 0

    # White is positive, Black is negative
    return whiteScore - blackScore + random.randint(-100, 100)/100

if __name__ == '__main__':
    board = chess.Board()

    while(board.is_checkmate() == False):
        print(board)
        move = input("White enter a move")
        # TODO: Check invald moves
        while chess.Move.from_uci(move) not in board.legal_moves:
            move = input("Illegal move, enter another move")
        board.push_uci(move)
        print(board)
        tree = TreeNode.Node(board, None)
        TreeNode.makeTree(tree, 3)
        #TreeNode.printTree(tree)
        #move = TreeNode.minimax(tree, 4, False) # False since trying to minimize
        move = TreeNode.abpruning(tree, 3, -10000000, 10000000, False)  # False since trying to minimize
        board.push_uci(str(move.move))
    print("game over")


