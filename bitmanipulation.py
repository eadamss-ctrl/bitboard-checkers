class BitManipulation:
    def __init__(self):
        pass

    # Set a bit at the given position
    def set_bit(self, num, pos):
        return num | (1 << pos)

    # Clear a bit at the given position
    def clear_bit(self, num, pos):
        return num & ~(1 << pos)

    # Toggle a bit at the given position
    def toggle_bit(self, num, pos):
        return num ^ (1 << pos)

    # Check if a bit is set at a given position
    def is_bit_set(self, num, pos):
        return (num >> pos) & 1

    # Count the number of 1s in the binary representation
    def count_ones(self, num):
        return bin(num).count('1')

    # Perform bitwise AND
    def bitwise_and(self, num1, num2):
        return num1 & num2

    # Perform bitwise OR
    def bitwise_or(self, num1, num2):
        return num1 | num2

    # Perform bitwise XOR
    def bitwise_xor(self, num1, num2):
        return num1 ^ num2

    # Left shift operation
    def left_shift(self, num, shifts):
        return num << shifts

    # Right shift operation
    def right_shift(self, num, shifts):
        return num >> shifts
