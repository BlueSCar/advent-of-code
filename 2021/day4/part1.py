from typing import List

def create_board(raw_board: str):
    return [[dict(number=int(n), marked=False) for n in row.split()] for row in raw_board.split('\n')]

def mark_board(number: int, board: List[List[dict]]):
    for row in board:
        for column in row:
            if column['number'] == number:
                column['marked'] = True

def evaluate_board(board: List[List[dict]]):
    for row in board:
        if all([number['marked'] for number in row]):
            return True
        
    for i in range(5):
        if all([row[i]['marked'] for row in board]):
            return True
        
    return False

def score_board(board: List[List[dict]]):
    return sum(column['number'] for row in board for column in row if not column['marked'])

file = open('day4/input.txt')
sections = file.read().split('\n\n')

number_draw = [int(n) for n in sections[0].split(',')]
boards = [create_board(board) for board in sections[1:]]

def play_bingo():
    for number in number_draw:
        for board in boards:
            mark_board(number, board)
            if evaluate_board(board):
                return score_board(board) * number
    
score = play_bingo()

print(score)