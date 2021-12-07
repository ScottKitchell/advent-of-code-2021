from copy import deepcopy
import day_4_data as DATA

BOARD_SIZE = 5


def run_tests(function, test_data):
  for numbers, board, expected_val in test_data:
    val = function(board, numbers)
    assert val == expected_val, \
      "{}: {} does not equal {}".format(function.__name__, val, expected_val)


def find_winning_board(boards, numbers):
  boards_copy = deepcopy(boards)  # so we can mutate it
  
  for num in numbers:
    for board_i, board in enumerate(boards_copy):
      cols_complete = [True for i in range(BOARD_SIZE)]
      rows_complete = [True for i in range(BOARD_SIZE)]

      for row_i, row in enumerate(board):
        for col_i, val in enumerate(row):
          if num == val:
            board[row_i][col_i] = None
          elif val is not None:
            rows_complete[row_i] = False
            cols_complete[col_i] = False

      if any(rows_complete) or any(cols_complete):
        print(f"Board {board_i} won after number {num}", board)
        return score_board(board, num)

  print("Error: No winning board")


def find_losing_board(boards, numbers):
  boards_copy = deepcopy(boards)  # so we can mutate it
  boards_complete = [False for i in range(len(boards_copy))]
  
  for num in numbers:
    for board_i, board in enumerate(boards_copy):
      cols_complete = [True for i in range(BOARD_SIZE)]
      rows_complete = [True for i in range(BOARD_SIZE)]

      for row_i, row in enumerate(board):
        for col_i, val in enumerate(row):
          if num == val:
            board[row_i][col_i] = None
          elif val is not None:
            rows_complete[row_i] = False
            cols_complete[col_i] = False

      if any(rows_complete) or any(cols_complete):
        boards_complete[board_i] = True
        
        if all(boards_complete):
          print(f"Board {board_i} won last after number {num}", board)
          return score_board(board, num)

  print("Error: No losing board")


def score_board(board, num):
  remaining_sum = sum(sum(filter(None, row)) for row in board)
  print("remaining_sum", remaining_sum)
  score = remaining_sum * num
  print("score", score)
  return score


if __name__ == '__main__':
  print('Testing...')
  run_tests(find_winning_board, DATA.WINNING_TESTS)
  run_tests(find_losing_board, DATA.LOSING_TESTS)
  print('Testing complete')

  find_winning_board(DATA.BOARDS, DATA.NUMBERS)
  find_losing_board(DATA.BOARDS, DATA.NUMBERS)
