with open('4/input.txt') as f:
    numbers = f.readline().split(',')
    numbers = [int(n) for n in numbers]
    f.readline()
    board_vals = []
    for vals in f.read().split('\n\n'):
        board = []
        for row in vals.split('\n'):
            int_row = [int(r) for r in row.split()]
            board.append(int_row)
        board_vals.append(board)


class Bingo():

    def __init__(self, rows):
        self.board = rows
        self.n = len(rows)
        self.called = [[False for _ in r] for r in rows]
        self.v_to_coord = {}
        for i in range(self.n):
            for j in range(self.n):
                self.v_to_coord[rows[i][j]] = (i, j)

    def add_called(self, v):
        if v not in self.v_to_coord:
            return False

        i, j = self.v_to_coord[v]
        self.called[i][j] = True
        return True
    
    def get_unmarked(self):
        return [self.board[i][j] for i in range(self.n) for j in range(self.n) if not self.called[i][j]]

    def is_bingo(self):
        for i in range(self.n):
            if all(self.called[i]):
                return True
        for j in range(self.n):
            column = [self.called[i][j] for i in range(self.n)]
            if all(column):
                return True
        return False


def part_1():
    boards = [Bingo(board) for board in board_vals]
    first_bingo = None
    for num in numbers:
        if first_bingo is not None:
            break
        for board in boards:
            if board.add_called(num) and board.is_bingo():
                return num * sum(board.get_unmarked())
    return 'No Bingo Found.'

def part_2():
    boards = [Bingo(board) for board in board_vals]
    board_nums = [i for i in range(len(boards))]
    for num in numbers:
        rerun_boards = []
        for board_n in board_nums:
            board = boards[board_n]
            if not(board.add_called(num) and board.is_bingo()):
                rerun_boards.append(board_n)
            elif len(board_nums) == 1:
                return num * sum(board.get_unmarked())
        board_nums = rerun_boards
    return 'No Bingo Found.'

print(part_1())
print(part_2())
