from collections import defaultdict


class Line:
    def __init__(self, line):
        self.x1, self.y1, self.x2, self.y2 = self.extract_coords(line)
        self.line_pos = []

    def compute_line(self, diagonal=False):
        if self.x1 == self.x2 or self.y1 == self.y2:
            # Handle horizontal or vertical lines
            x_step = 1 if self.x2 >= self.x1 else -1
            y_step = 1 if self.y2 >= self.y1 else -1
            xs = range(self.x1, self.x2 + x_step, x_step) if self.x1 != self.x2 else [self.x1] * (abs(self.y2 - self.y1) + 1)
            ys = range(self.y1, self.y2 + y_step, y_step) if self.y1 != self.y2 else [self.y1] * (abs(self.x2 - self.x1) + 1)
            self.line_pos = ((x, y) for x, y in zip(xs, ys))
        elif diagonal:
            # Handle diagonal lines
            x_step = 1 if self.x2 >= self.x1 else -1
            y_step = 1 if self.y2 >= self.y1 else -1
            xs = range(self.x1, self.x2 + x_step, x_step)
            ys = range(self.y1, self.y2 + y_step, y_step)
            self.line_pos = ((x, y) for x, y in zip(xs, ys))

    @staticmethod
    def extract_coords(line: str) -> tuple[int, int, int, int]:
        first_part, second_part = line.split(" -> ")
        x1, y1 = first_part.split(",")
        x2, y2 = second_part.split(",")
        return int(x1), int(y1), int(x2), int(y2)

def compute_score(pos: dict[tuple[int, int], int]):
    return sum(1 for v in pos.values() if v > 1)


def part1(lines, diagonal=False):
    tot_pos = defaultdict(int)
    line_instances = [Line(l_str) for l_str in lines]
    
    for l in line_instances:
        l.compute_line(diagonal=diagonal)
        for pos in l.line_pos:
            tot_pos[pos] += 1
    return compute_score(tot_pos)


def main():
    with open("day5.data", "r") as f:
        lines = [line.strip() for line in f]
    print(part1(lines))
    print(part1(lines, diagonal=True))


if __name__ == "__main__":
    main()