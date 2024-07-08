import numpy as np


def numpy_array_to_text(np_array, base):
    # Convert each base representation string back to an integer
    unicode_values = [int(value, base) for value in np_array]

    # Convert each integer (Unicode value) to its corresponding character
    chars = [chr(value) for value in unicode_values]

    # Join all characters to form the final string
    text = ''.join(chars)

    return text



