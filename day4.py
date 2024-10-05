def getBoards(lines: list[str]) -> list[list[str]]:
  # lines must start with a board
  boards =  []
  curr_board = []
  for l in lines:
    l = l.strip() 
    if l == "": # separation line
      boards.append(curr_board)
      curr_board = []
    else:
      curr_board.append(l)
  return boards



def part1(numbers: list[str], boards: list[list[str]]) -> int:
  res_cols = {}
  res_rows = {}
  for n in numbers:
    for i, board in enumerate(boards):
      for row_nb, row in enumerate(board):
        digits = row.strip().split()
        for col_nb, digit in enumerate(row.strip().split()):
          if digit == n:
            res_rows[(i, row_nb)] = res_rows.get((i, row_nb), 0) + 1
            res_cols[(i, col_nb)] = res_cols.get((i, col_nb), 0) + 1
            digits[col_nb] += "X" # cross the digit so it wont be computed in the result
            boards[i][row_nb] = " ".join(digits)
            if res_rows[(i, row_nb)] == 5 or res_cols[i, col_nb] == 5:
              return evaluate_board(n, board)

def part2(numbers: list[str], boards: list[list[str]]) -> int:
  nb_finished = 0
  finished_boards = set() 
  res_cols = {}
  res_rows = {}
  for n in numbers:
    for i, board in enumerate(boards):
      if i not in finished_boards:
        for row_nb, row in enumerate(board):
          digits = row.strip().split()
          for col_nb, digit in enumerate(row.strip().split()):
            if digit == n:
              res_rows[(i, row_nb)] = res_rows.get((i, row_nb), 0) + 1
              res_cols[(i, col_nb)] = res_cols.get((i, col_nb), 0) + 1
              digits[col_nb] += "X" # cross the digit so it wont be computed in the result
              boards[i][row_nb] = " ".join(digits)
              if res_rows[(i, row_nb)] == 5 or res_cols[i, col_nb] == 5:
                nb_finished += 1
                finished_boards.add(i)
                if nb_finished == len(boards):
                  return evaluate_board(n, board)


def evaluate_board(n, board):
  sum = 0
  for row in board:
    for digit in row.strip().split():
      if "X" not in digit:
        sum+=int(digit)
  return int(n) * sum


def main():
  with open("day4.data", "r") as f:
    lines = f.readlines()
  print(part1(lines[0].split(","), getBoards(lines[2:])))
  print(part2(lines[0].split(","), getBoards(lines[2:])))
  


if __name__ == "__main__":
  main()