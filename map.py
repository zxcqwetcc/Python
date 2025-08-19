# создаём пустое поле 3x3
board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]

# функция для печати поля
def print_board(board):
    for row in board:
        print(" | ".join(row))

# функция для хода игрока
def make_move(board, row, col, symbol):
    if board[row][col] == "_":  # если клетка пустая
        board[row][col] = symbol
    else:
        print("Клетка уже занята!")

# тест
print("Начальное поле:")
print_board(board)

make_move(board, 0, 0, "X")
make_move(board, 0, 1, "X" )
make_move(board, 0, 2, "X")

print("\nПосле ходов:")
print_board(board)
