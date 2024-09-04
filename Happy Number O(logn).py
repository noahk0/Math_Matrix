def isHappy(self, n: int) -> bool:
    seen = set()

    while 1 < n:
        new = 0
        seen.add(n)

        while n:
            new += (n % 10) ** 2
            n //= 10

        if new in seen:
            return False

        n = new

    return True
