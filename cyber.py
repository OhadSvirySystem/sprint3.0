import os
import qrcode
import cv2

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

    txt_list = []
    # Read and print the contents of each .txt file
    for file in txt_files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            txt_list.append(content)

    return txt_list


def generate_qr_code(text, index):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f'qr_code_{index}.png')


def display_qr_codes(text_list):
    cv2.waitKey(4000)
    for index, text in enumerate(text_list):
        generate_qr_code(text, index)
        img = cv2.imread(f'qr_code_{index}.png')
        cv2.imshow('QR Code', img)
        cv2.waitKey(2000)  # Display each QR code for 1 second
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Define the directory path

    directory_path = "C:\\Users\\TLP-001\\Downloads\\top_secret"
    #directory_path = r"C:\Users\Public\Documents\top_secret"

    # Call the function to read .txt files from the specified directory
    txt_list = read_txt_files(directory_path)
    display_qr_codes(txt_list)

