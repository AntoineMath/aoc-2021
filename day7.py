import math
import functools

def part1(line: list[str]) -> int:
  nbs = [int(i) for i in line.strip().split(",")]
  nbs = sorted(nbs)
  median = nbs[len(nbs)//2]
  # return the sum for each crab to move to the pos 
  return sum(abs(nb-median) for nb in nbs) 


def part2(line: str) -> int:
  d = {}
  for n in line.strip().split(","):
    d[int(n)] = d.get(int(n), 0) + 1
  min_cost = float("inf") 
  best_pos = 0

  def triangular_cost(n: int) -> int:
    return n * (n+1) / 2

  for pos in range(0, max(d)+1):
    pos_cost = 0
    for curr_pos, v in d.items():
      pos_cost += triangular_cost(abs(curr_pos - pos)) * v # used to approximate
    if pos_cost < min_cost:
      min_cost = pos_cost
      best_pos = pos

  final_res = 0
  for curr_pos, v in d.items():
    final_res += functools.reduce(lambda a, b: a + b, range(abs(curr_pos - best_pos) + 1), 0) * v  # real computation
  return final_res 

       


def main():
  with open("day7.data", "r") as f:
    lines = f.readlines()
  print(part1(lines[0]))
  print(part2(lines[0]))
  


if __name__ == "__main__":
  main()