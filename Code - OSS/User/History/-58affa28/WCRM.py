# Authors: Marta Prati  - S5139155 and Amaia Lagarde - S5204690
# This program determines whether a fir filter is implemented
# Prints the filter's impulse response in case it is


# Read signal + length
def readSignal():
    input_line = input().strip()
    length = int(input_line.split(":")[0])
    signal = list(map(int, input_line.split(":")[1].strip()[1:-1].split(",")))
    return signal, length


# Print signal + length
def printSignal(length, signal):
    print(f"{length}: {signal}")


def column_sum(h, x, n, h_lenght, x_length):
    sum_column = 0

    for z in range(n):
        if z < h_lenght and (n - z) < x_length:
            # Sum of all numbers in that column
            sum_column += h[z] * x[n - z]
    return sum_column


def find_impulse_response(x, x_length, y, y_length):
    # Initilizes array of impulses with given lenght
    h = []
    h_lenght = y_length - x_length + 1

    for n in range(y_length):
        sum_column = 0

        if n != 0:  # First coeffiecent is equal to y[0]/x[0] coefficent
            sum_column = column_sum(h, x, n, h_lenght, x_length)

        impulse_difference = y[n] - sum_column

        if n < h_lenght:
            # Append value only if withing the range of lenght
            h_value = impulse_difference / x[0]
            h.append(int(h_value))

        print(int(impulse_difference / x[0]))
        # Not a FIR system is any column after last impulse does not equal to corresponding y[n] value
        if n > h_lenght - 1 and impulse_difference != 0:
            return

    # It is FIR system
    return h


def main():
    x, x_length = readSignal()
    y, y_length = readSignal()

    result = find_impulse_response(x, x_length, y, y_length)
    print(result)
    if result is None:
        print("NOT FIR")
    else:
        printSignal(len(result), result)


if __name__ == "__main__":
    main()
