
def part1(line: list[str]) -> int:
  nbs = [int(i) for i in line.strip().split(",")]
  nbs = sorted(nbs)
  median = nbs[len(nbs)//2]
  # return the sum for each crab to move to the pos 
  return sum(abs(nb-median) for nb in nbs) 


def part2(lines: list[str]) -> int:
  pass


def main():
  with open("day7.data", "r") as f:
    lines = f.readlines()
  print(part1(lines[0]))
  


if __name__ == "__main__":
  main()