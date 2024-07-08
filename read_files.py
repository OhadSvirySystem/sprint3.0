import os
#hello


def read_txt_files(directory):
    # Check if the specified directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # List all files in the directory
    files = os.listdir(directory)


    # Filter for files that end with .txt
    txt_files = [file for file in files if file.endswith('.txt')]

    # If no .txt files found, print a message
    if not txt_files:
        print("No .txt files found in the directory.")
        return

    # Read and print the contents of each .txt file
    for file in txt_files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"Contents of {file}:\n{content}")


if __name__ == "__main__":
    # Define the directory path

    directory_path = r"C:\Users\TLP-001\PythonProjects\semester2\sprint"
    #directory_path = r"C:\Users\Public\Documents\top_secret"

    # Call the function to read .txt files from the specified directory
    read_txt_files(directory_path)

