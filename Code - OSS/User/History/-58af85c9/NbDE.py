# Authors: Marta Prati  - S5139155 and Amaia Lagarde - S5204690

import cmath
import math


def get_input_data():
    input_1, input_2, input_3 = map(int, input().split())
    return input_1, input_2, input_3


def readSignal():
    input_line = input().strip()
    length = int(input_line.split(":")[0])
    signal = list(map(int, input_line.split(":")[1].strip()[1:-1].split(",")))
    return signal, length


def get_input_data():
    input_1, input_2, input_3 = map(float, input().split())
    return input_1, input_2, input_3


def printOutput(Ay, omega, phi_y):
    if Ay <= 0.04:
        print("y[n]= 0.00")
    else:
        print(f"y[n]={Ay:.2f}cos({omega:.2f}*n{phi_y:+.2f})")


def gain(h, h_length, omega):
    gain_h = 0  # Initialize gain_h before using it
    angle_gain = 0

    for n in range(h_length):
        gain_h += h[n] * cmath.exp(-1j * n * omega)
        angle_gain += h[n] * cmath.exp(-1j * n * omega) * (-n)

    return abs(gain_h), cmath.phase(gain_h)


# Slide 19 - lecture 5
def fir_for_sinusoid(Ax, phi_x, gain_h, angle_gain):
    # The amplitude A is multiplied by the gain |H(eˆjω)| < 1
    Ay = Ax * gain_h
    # The phase φ is increased by H(eˆjω). Get only the real part.
    phi_y = phi_x + angle_gain

    # Ensure the phase is within the range -π < φ_y ≤ π
    if phi_y <= -math.pi:
        phi_y += 2 * math.pi
    elif phi_y > math.pi:
        phi_y -= 2 * math.pi
    return Ay, phi_y


def main():
    h, h_length = readSignal()
    Ax, omega, phi_x = get_input_data()
    gain_h, angle_gain = gain(h, h_length, omega)
    Ay, phi_y = fir_for_sinusoid(Ax, phi_x, gain_h, angle_gain)
    printOutput(Ay, omega, phi_y)


if __name__ == "__main__":
    main()
