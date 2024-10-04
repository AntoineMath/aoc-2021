
def part1(lines: list[str]) -> int:
  h, v = 0, 0
  for l in lines:
    direction, amount = l.split()
    if direction == "forward":
      h += int(amount)
    if direction == "up":
      v-=int(amount)
    if direction == "down":
      v+=int(amount)
  return h*v

def part2(lines: list[str]) -> int:
  h, d , aim = 0, 0, 0
  for l in lines:
    direction, amount = l.split()
    amount = int(amount)
    if direction == "forward":
      h += amount
      d += aim * amount
    if direction == "up":
      aim -= amount
    if direction == "down":
      aim += amount
  return h*d


def main():
  with open("day2.data", "r") as f:
    lines = f.readlines()
  print(part1(lines))
  print(part2(lines))
  


if __name__ == "__main__":
  main()