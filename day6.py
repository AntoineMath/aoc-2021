import collections
def part1(line: str, iters: int, bryan_johnson: bool = False) -> list[str]:
  lfs = list(map(lambda x : int(x), line.strip().split(",")))
  for _ in range(iters):
    to_append: list[int] = []
    for i, lf in enumerate(lfs):
      if lf > 0:
        lfs[i] -= 1
      else:
        lfs[i] = 6
        to_append.append(8)
    lfs.extend(to_append)
  print(len(lfs))

def part2(line: str, iters: int) -> list[str]:
  fish_timer = collections.deque([0]*9) # index represent timer and value the nb of fish with this timer
  for nb in line.strip().split(","):
    fish_timer[int(nb)] += 1
  
  for _ in range(iters):
    new_fish = fish_timer.popleft()
    fish_timer[6] += new_fish # reset fish to timer 6
    fish_timer.append(new_fish)
  return sum(fish_timer)


  

  




def main():
  with open("day6.data", "r") as f:
    lines = f.readlines()
  part1(lines[0], 80) # only one line
  print(part2(lines[0], 256)) # only one line
  


if __name__ == "__main__":
  main()