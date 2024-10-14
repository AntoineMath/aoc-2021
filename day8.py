def part1(lines: list[str]) -> list[str]:
  #num_to_seg_nb = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
  dig_to_nb_seg = {
    "2": 1,
    "4": 4,
    "3": 7,
    "7": 8
  }
  tot = 0
  for l in lines:
    #obs = l.split(" | ")[0].strip().split(" "), 
    outs = l.split(" | ")[1].strip().split(" ")
    print(outs)
    for o in outs:
      print(str(len(o)))
      if str(len(o)) in dig_to_nb_seg:
        tot += 1
  return tot

def part2(line: str, iters: int) -> list[str]:
  pass


def main():
  with open("day8.data", "r") as f:
    lines = f.readlines()
  print(part1(lines))
  

if __name__ == "__main__":
  main()