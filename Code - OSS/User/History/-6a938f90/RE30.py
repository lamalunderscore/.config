import cmath
import math


def readSignal():
    input_line = input().strip()
    length = int(input_line.split(":")[0])
    signal = list(map(int, input_line.split(":")[1].strip()[1:-1].split(",")))
    return signal, length


def printSignal(length, signal):
    print(f"{length}: {signal}")


def frequency_response(h: list) -> tuple:
    response = 0
    for n in range(len(h)):
        response += h[n] * cmath.exp(-1j * n * omega)


def output_frequency(a_x, p_x, radian, h) -> str:
    magnitude, angle = frequency_response(h)


def is_finite(h: list, h_len) -> bool:
    # return the truth value of the validity for the list of coefficients h
    return not any(h[h_len:])


if __name__ == "__main__":
    x, x_len = readSignal()
    y, y_len = readSignal()
    h = reverse_fir(x, y)
    h_len = y_len - x_len + 1
    if is_finite(h, h_len):
        # turn all values of h to int and
        # adjust its length to the valid values
        h = [int(i) for i in h[:h_len]]
        printSignal(len(h), h)
    else:
        print("NO FIR")