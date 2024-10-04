
def part1(lines: list[str]) -> int:
  ones = [0] * (len(lines[0])-1)
  zeros = [0] * (len(lines[0])-1)
  for l in lines:
    for i, c in enumerate(list(l)):
      if c == "0":
        zeros[i] += 1
      if c == "1":
        ones[i] += 1

  y_rate = [one > zero for (one, zero) in zip(ones, zeros)]
  y_rate_str = "".join("1" if b else "0" for b in y_rate) 
  e_rate_str = "".join("0" if b else "1" for b in y_rate) 


  return int(y_rate_str, 2) * int(e_rate_str, 2)

  



def part2(lines: list[str]) -> int:
    oxygen_lines, co2_lines = lines[:], lines[:]
    
    # Oxygen generator rating
    for i in range(len(lines[0].strip())):
        if len(oxygen_lines) > 1:
            ones = sum(1 for l in oxygen_lines if l[i] == "1")
            zeros = len(oxygen_lines) - ones
            
            # Keep the most common bit, or keep '1' if there is a tie
            if ones >= zeros:
                oxygen_lines = [l for l in oxygen_lines if l[i] == "1"]
            else:
                oxygen_lines = [l for l in oxygen_lines if l[i] == "0"]

    # CO2 scrubber rating
    for i in range(len(lines[0].strip())):
        if len(co2_lines) > 1:
            ones = sum(1 for l in co2_lines if l[i] == "1")
            zeros = len(co2_lines) - ones
            
            # Keep the least common bit, or keep '0' if there is a tie
            if ones >= zeros:
                co2_lines = [l for l in co2_lines if l[i] == "0"]
            else:
                co2_lines = [l for l in co2_lines if l[i] == "1"]
    
    # Convert binary strings to integers and multiply the results
    oxygen = int(oxygen_lines[0].strip(), 2)
    co2 = int(co2_lines[0].strip(), 2)
    return oxygen * co2

  


def main():
  with open("day3.data", "r") as f:
    lines = f.readlines()
  print(part1(lines))
  print(part2(lines))
  


if __name__ == "__main__":
  main()