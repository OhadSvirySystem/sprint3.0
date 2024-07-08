import numpy as np


def text_to_numpy_array(input_file, base):
    # Read the text file with UTF-8 encoding
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Convert each character to its Unicode (ASCII) value
    unicode_values = [ord(char) for char in text]

    # Create a list of base-representations from the Unicode values
    array = [np.base_repr(value, base) for value in unicode_values]

    return array



