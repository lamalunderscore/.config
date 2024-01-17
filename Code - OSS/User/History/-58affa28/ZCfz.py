# Authors: Marta Prati  - S5139155 and Amaia Lagarde - S5204690
# This program determines whether a fir filter is implemented
# Prints the filter's impulse response in case it is

# Read signal + length
def readSignal():
    input_line = input().strip()
    length = int(input_line.split(':')[0])
    signal = list(map(int, input_line.split(':')[1].strip()[1:-1].split(',')))
    return signal, length


# Print signal + length
def printSignal(length, signal):
    print(f"{length:.0f}: {signal}")


def find_impulse_response_(x, x_length, y, y_length):
    h_length = y_length - x_length + 1
    h = []

    for n in range(y_length):
        sum_column = 0
        if n != 0:
            h_range = n
            for z in range(h_range):
                if (n - z) < x_length:
                    sum_column += h[z] * x[n-z]

        impulse_difference = (y[n] - sum_column)

        h_value = impulse_difference / x[0]
        h.append(int(h_value))

        if n == h_length and impulse_difference == 0:
            return h

    return


def main():
    x, x_length = readSignal()
    y, y_length = readSignal()

    result = find_impulse_response_(x, x_length, y, y_length)
    if not result:
        print("NOT FIR")
    else:
        printSignal(len(result), result)


if __name__ == "__main__":
    main()
