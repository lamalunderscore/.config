def readSignal():
    input_line = input().strip()
    length = int(input_line.split(":")[0])
    signal = list(map(int, input_line.split(":")[1].strip()[1:-1].split(",")))
    return signal, length


def printSignal(length, signal):
    print(f"{length}: {signal}")


def reverse_fir(x: list, x_len: int, y: list, y_len: int) -> list:
    h = list()
    for n in range(y_len):
        deduction = 0
        for i in range(n):
            try:
                deduction += h[i] * x[n - i]
            except IndexError:
                deduction = 0
        h.append(int((y[n] - deduction) / x[0]))
    return h


def is_finite(h: list) -> bool:
    if h[-1] != 0:
        return False
    return True


if __name__ == "__main__":
    x, x_len = readSignal()
    y, y_len = readSignal()
    h = reverse_fir(x, x_len, y, y_len)
    if is_finite(h):
        print(f"{len(h) - 1}: ", h[:-1])
    else:
        print("NOT FIR")
