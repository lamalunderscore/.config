import cmath
import math


def readSignal():
    input_line = input().strip()
    length = int(input_line.split(":")[0])
    signal = list(map(int, input_line.split(":")[1].strip()[1:-1].split(",")))
    return signal, length


def get_input_data():
    input_1, input_2, input_3 = map(float, input().split())
    return input_1, input_2, input_3


def magnitude_angle(h: list, radian: float) -> tuple:
    frequency_response = 0
    for n in range(len(h)):
        # this calculates the frequency response in exponential form
        frequency_response += h[n] * cmath.exp(-1j * n * radian)
    # we return the magnitude (abs()) and angle (cmath.phase)
    # of the frequency response
    return abs(frequency_response), cmath.phase(frequency_response)


def range_phi(phi: float) -> float:
    # this function sets phi in the range of (-pi, pi]
    if phi <= -math.pi:
        return range_phi(phi + 2 * math.pi)
    if math.pi < phi:
        return range_phi(phi - 2 * math.pi)
    return phi


def output_signal(amplitude_x, phi_x, radian, h) -> str:
    magnitude, angle = magnitude_angle(h, radian)

    amplitude_y = amplitude_x * magnitude

    phi_y = phi_x + angle
    phi_y = range_phi(phi_y)

    y = "y[n]="
    if round(amplitude_y, 2) == 0:
        return y + "0.00"
    return y + f"{amplitude_y:.2f}cos({radian:.2f}*n{phi_y:.2f})"

def combine_fir(h1:list, h2: list)-> list:
    

if __name__ == "__main__":
    h1 = readSignal()
    h2 = readSignal()
    h = combine_fir(h1[0], h2[0])
    amplitude_x, radian, phi_x = get_input_data()
    print(output_signal(amplitude_x, phi_x, radian, h[0]))