import os
from txt_to_base import text_to_numpy_array
from base_to_txt import numpy_array_to_text
from receive import*
from transmit import*


def return_txt_files(directory):
    # Check if the specified directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # List all files in the directory
    files = os.listdir(directory)


    # Filter for files that end with .txt
    txt_files = [os.path.join(directory, file) for file in files if file.endswith('.txt')]

    # If no .txt files found, print a message
    if not txt_files:
        print("No .txt files found in the directory.")
        return

    # Read and print the contents of each .txt file
    return txt_files


if __name__ == "__main__":
    # Define the directory path

    directory_path = r"C:\Users\TLP-001\PythonProjects\semester2\sprint\sprint3.0\top_secret"
    #directory_path = r"C:\Users\Public\Documents\top_secret"

    txt_files = return_txt_files(directory_path)

    for txt_file in txt_files:
        base = 2

        np_array = text_to_numpy_array(txt_file, base)
        print(np_array)

        text = numpy_array_to_text(np_array, base)
        print(text)




