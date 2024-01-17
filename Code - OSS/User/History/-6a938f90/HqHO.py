import cmath
import math


def readSignal():
    input_line = input().strip()
    length = int(input_line.split(":")[0])
    signal = list(map(int, input_line.split(":")[1].strip()[1:-1].split(",")))
    return signal, length


def printSignal(length, signal):
    print(f"{length}: {signal}")


def magnitude_angle(h: list, radian: float) -> tuple:
    frequency_response = 0
    for n in range(len(h)):
        # this calculates the frequency response in exponential form
        frequency_response += h[n] * cmath.exp(-1j * n * radian)
    # we return the magnitude (abs()) and angle (cmath.phase)
    # of the frequency response
    return abs(frequency_response), cmath.phase(frequency_response)


def range_phi(f: float) -> float:
    # this function sets f in the range of (-0.5, 0.5]
    if -1 >= f:
        return alias(f + 1)
    if 0.5 < f:
        return alias(f - 1)
    return f


def output_frequency(amplitude_x, phi_x, radian, h) -> str:
    magnitude, angle = magnitude_angle(h, radian)

    amplitude_y = amplitude_x * magnitude

    phi_y = phi_x + angle
    range_phi(phi_y)


if __name__ == "__main__":
    x, x_len = readSignal()
    y, y_len = readSignal()
