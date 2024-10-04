

def part1(lines: list[str]) -> int:
  res = 0
  for i in range(1, len(lines)):
    if int(lines[i]) > int(lines[i-1]):
      res+=1
  return res

def part2(lines: list[str]) -> int:
  res = 0
  curr_sum = 0
  prev = 0
  for i in range(len(lines)-3):
    for c in range(3):
      curr_sum += int(lines[i+c])
    if curr_sum > prev:
      res+=1
    prev = curr_sum 
    curr_sum = 0
  return res


def main():
  with open("day1.data", "r") as f:
    lines = f.readlines()
  print(part1(lines))
  print(part2(lines))
  


if __name__ == "__main__":
  main()