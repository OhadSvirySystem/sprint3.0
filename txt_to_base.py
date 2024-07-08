import numpy as np


def text_to_numpy_array(input_file, base):
    # Read the text file
    with open(input_file, 'r') as file:
        text = file.read()

    # Convert each character to its ASCII value
    ascii_values = [ord(char) for char in text]

    # Create a NumPy array from the ASCII values
    np_array = np.array([np.base_repr(value, base) for value in ascii_values])

    return np_array



