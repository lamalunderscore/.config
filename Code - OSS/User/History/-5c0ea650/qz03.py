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
        print("n: ", n)
        deduction = 0
        for i in range(n):
            print("i: ", i)
            deduction += h[i] * x[n - i]
        h.append((y[n] - deduction) / x[0])
    print(h)
    return h


if __name__ == "__main__":
    x, x_len = readSignal()
    y, y_len = readSignal()
    print(reverse_fir(x, x_len, y, y_len))
