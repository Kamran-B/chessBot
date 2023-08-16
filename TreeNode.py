import copy
import chess

import main


class Node:

    def __init__(self, board, move):
        self.board = board
        self.score = main.evaluate(board)
        self.move = move
        self.children = []


def makeTree(root, depth, level=1):
    # Generates the tree of possible moves

    # print(root.board)
    if depth <= 0:
        root.children = []
        return
    # print("tree")
    # print(list(root.board.legal_moves))
    legalMoves = list(root.board.legal_moves)
    for move in legalMoves:
        # print("    leaf  " + str(move))
        new = Node(copy.copy(root.board), move if level == 1 else root.move)
        new.board.push_uci(move.uci())
        makeTree(new, depth - 1, level + 1)
        root.children.append(new)


def minimax(pos, depth, maxPlayer):
    # Basic minimax function to determine the best position from the tree
    if depth == 0 or len(pos.children) == 0:  # or game over in pos
        return pos
    if maxPlayer:
        maxEval = pos.children[0].score
        maxPos = pos.children[0]
        for i in pos.children:
            best = minimax(i, depth - 1, False)
            if maxEval < best.score:
                maxEval = best.score
                maxPos = best
        return maxPos
    else:
        minEval = pos.children[0].score
        minPos = pos.children[0]
        for i in pos.children:
            best = minimax(i, depth - 1, True)
            if minEval > best.score:
                minEval = best.score
                minPos = best
        return minPos

def abpruning(pos, depth, alpha, beta, maxPlayer):
    # Alpha Beta pruning function to speed up minimax
    if depth == 0 or len(pos.children) == 0:  # or game over in pos
        return pos
    if maxPlayer:
        maxEval = pos.children[0].score
        maxPos = pos.children[0]
        for i in pos.children:
            best = abpruning(i, depth - 1, alpha, beta, False)
            if maxEval < best.score:
                maxEval = best.score
                maxPos = best
            alpha = max(alpha, best.score)
            if beta <= alpha:
                break
        return maxPos
    else:
        minEval = pos.children[0].score
        minPos = pos.children[0]
        for i in pos.children:
            best = abpruning(i, depth - 1, alpha, beta, True)
            if minEval > best.score:
                minEval = best.score
                minPos = best
            beta = min(beta, best.score)
            if beta <= alpha:
                break
        return minPos


def printTree(tree):
    # Prints out the contents of the tree (NOT WORKING)
    print(tree.score, len(tree.children))
    for child in tree.children:
        printTree(child)
