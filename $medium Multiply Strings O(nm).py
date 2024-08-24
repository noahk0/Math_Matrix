def multiply(self, num1: str, num2: str) -> str:
    if num1 == '0' or num2 == '0':
        return '0'
            
    num, num1, num2, res = '', num1[::-1], num2[::-1], [0] * (len(num1) + len(num2))

    for i in range(len(num1)):
        for j in range(len(num2)):
            res[i + j] += int(num1[i]) * int(num2[j])

    for i in range(1, len(res)):
        num = str(res[i - 1] % 10) + num
        res[i] += res[i - 1] // 10

    return str(res[-1]) + num if res[-1] else num
