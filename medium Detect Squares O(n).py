class DetectSquares:

    def __init__(self):
        self.plane = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.plane[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        count = 0

        for y in self.plane[point[0]]:
            if x := abs(point[1] - y):
                count += self.plane[point[0]][y] * (self.plane[point[0] + x][y] * self.plane[point[0] + x][point[1]] + self.plane[point[0] - x][y] * self.plane[point[0] - x][point[1]])
            
        return count
