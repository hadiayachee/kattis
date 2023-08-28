def primonimo_game(n, m, p, board):
    def is_winning_state(board):
        return all(all(cell == p for cell in row) for row in board)
    
    def make_move(board, row, col):
        for i in range(n):
            board[i][col] = (board[i][col] % p) + 1
        for j in range(m):
            board[row][j] = (board[row][j] % p) + 1
    moves = []
    for row in range(n):
        for col in range(m):
            while not is_winning_state(board):
                if board[row][col] != p:
                    make_move(board, row, col)
                    moves.append((row, col))
    if is_winning_state(board):
        k = len(moves)
        return k, moves
    else:
        return -1
n, m, p = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = primonimo_game(n, m, p, board)
if result == -1:
    print(-1)
else:
    k, moves = result
    print(k)
    for move in moves:
        print(move[0] * m + move[1] + 1, end=' ')
