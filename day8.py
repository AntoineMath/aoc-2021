def part1(lines: list[str]) -> int:
  #num_to_seg_nb = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
  dig_to_nb_seg = {
    "2": 1,
    "4": 4,
    "3": 7,
    "7": 8
  }
  tot = 0
  for l in lines:
    outs = l.split(" | ")[1].strip().split(" ")
    for o in outs:
      if str(len(o)) in dig_to_nb_seg:
        tot += 1
  return tot


def part2(lines: list[str]) -> int:
  res = 0
  for l in lines: 
    nb_segment_map = {}
    ins = l.split(" | ")[0].strip().split(" ")

    nb_segment_map[1] = next(p for p in ins if len(p) == 2)
    nb_segment_map[7] = next(p for p in ins if len(p) == 3)
    nb_segment_map[4] = next(p for p in ins if len(p) == 4)
    nb_segment_map[8] = next(p for p in ins if len(p) == 7)

    fives = [p for p in ins if len(p) == 5] # 3, 5, 2
    sixes = [p for p in ins if len(p) == 6] # 0, 6, 9

    # 3 is the only 5 segment pattern that contains all of the segments of 1
    nb_segment_map[3] = next(p for p in fives if all(seg in p for seg in nb_segment_map[1]))

    # 9 is the only 5 segment pattern that contains all of the segments of 4
    nb_segment_map[9] = next(p for p in sixes if all(seg in p for seg in nb_segment_map[4]))

    # 0 is the only segment that contains all of the segments of 1 (that is not 9)
    nb_segment_map[0] = next(p for p in sixes if p!= nb_segment_map[9] and all(seg in p for seg in nb_segment_map[1]))

    # 6 is the last six-segment
    nb_segment_map[6] = next(p for p in sixes if p!=nb_segment_map[0] and p!= nb_segment_map[9])

    # 5 is the only 5-segment that contains 3 segments of 4
    nb_segment_map[5] = next(p for p in fives if p!=nb_segment_map[3] and len(set(nb_segment_map[4]) - set(p)) == 1)

    # 2 is the last one 
    nb_segment_map[2] = next(p for p in fives if p!=nb_segment_map[5] and p!=nb_segment_map[3])

    ## decode
    outs = l.split(" | ")[1].strip().split(" ")

    nums = [str(i) 
            for seg in outs
            for i in nb_segment_map 
            if set(nb_segment_map[i]) == set(seg)
    ]
    res += int(''.join(nums))
  return res
    


def main():
  with open("day8.data", "r") as f:
    lines = f.readlines()
  print(part1(lines))
  print(part2(lines))
  

if __name__ == "__main__":
  main()