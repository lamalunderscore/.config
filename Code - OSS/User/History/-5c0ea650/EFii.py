def readSignal():
    input_line = input().strip()
    length = int(input_line.split(":")[0])
    signal = list(map(int, input_line.split(":")[1].strip()[1:-1].split(",")))
    return signal, length


def printSignal(length, signal):
    print(f"{length}: {signal}")


def reverse_fir(x: list, y: list) -> list:
    h = list()
    for n in range(len(y)):
        deduction = 0
        for i in range(n):
            try:
                deduction += h[i] * x[n - i]
            except IndexError:
                deduction += 0
        h.append((y[n] - deduction) / x[0])
    return h


def is_finite(h: list, h_len) -> bool:
    return not any(h[h_len:])


if __name__ == "__main__":
    x, x_len = readSignal()
    y, y_len = readSignal()
    h = reverse_fir(x, y)
    h_len = y_len - x_len + 1
    if is_finite(h, h_len):
        print(f"{h_len}:", (int(i) for i in h[:h_len]))
    else:
        print("NO FIR")
