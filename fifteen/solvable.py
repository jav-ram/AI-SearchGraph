

def get_inv(board):
    inv_count = 0

    for j in range(0, len(board) - 1):
        for i in range(j + 1, len(board)):
            if board[j] > board[i]:
                if not board[i] == 0:
                    inv_count += 1

    return inv_count


def find_empty_position(board):
    for i in range(0, len(board)):
        if board[i] == 0 or board[i] == '0':
            return (i % 4) + 1


def is_solvable(board):
    inv_count = get_inv(board)
    empty = find_empty_position(board)
    print(inv_count)
    print(empty)

    if empty % 2 == 0:
        return inv_count % 2 == 1

    if empty % 2 == 1:
        return inv_count % 2 == 0
