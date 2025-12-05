import os
import numpy as np
import random

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def spawn_food(board):
    y = random.randint(0, len(board) - 1)
    x = random.randint(0, len(board[0]) - 1)
    if board[y][x] != 0:
        return spawn_food(board)
    board[y][x] = 1
    return board

def start_game(start=3, size=10):
    res = {
        "score": 0,
        "length": start,
        "board": [[0] * size] * size,
        "size": size
    }
    res["board"] = spawn_food(res["board"])
    return res

def draw(game):
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    GRAY = "\033[90m"
    
    print("+" + "-" * ( game["size"] * 2 + 1) + "+")
    for line in game["board"]:
        l = []
        for pixel in line:
            l.append([" ", f"{GREEN}#{RESET}", f"{YELLOW}*{RESET}"][pixel * 2])
        print("| " + " ".join(l) + " |")
    print("+" + "-" * ( game["size"] * 2 + 1) + "+")







os.system("clear")
print()

print("Hello World!")

game = start_game()

print(game)
draw(game)