def myPow(self, x: float, n: int) -> float:
    def exp(x, n):
        return exp(x * x, n // 2) * x if n % 2 else exp(x * x, n // 2) if n else 1

    return exp(x, n) if n > 0 else 1 / exp(x, -n)
