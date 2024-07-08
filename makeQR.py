import qrcode
import cv2
import numpy as np
from PIL import Image

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
    screen_res = (1920, 1080)  # Set this to your screen resolution
    for index, text in enumerate(text_list):
        generate_qr_code(text, index)
        qr_img = cv2.imread(f'qr_code_{index}.png')

        # Create a fullscreen window
        cv2.namedWindow('QR Code', cv2.WND_PROP_FULLSCREEN)
        
        cv2.imshow('QR Code', img,)
        cv2.setWindowProperty('QR Code', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # Create a black background image
        background = np.zeros((screen_res[1], screen_res[0], 3), dtype=np.uint8)

        # Calculate the position to center the QR code
        y_offset = (screen_res[1] - qr_img.shape[0]) // 2
        x_offset = (screen_res[0] - qr_img.shape[1]) // 2

        # Place the QR code on the background
        background[y_offset:y_offset + qr_img.shape[0], x_offset:x_offset + qr_img.shape[1]] = qr_img

        cv2.imshow('QR Code', background)
        cv2.waitKey(1000)  # Display each QR code for 1 second

    cv2.destroyAllWindows()

def read_string_from_file(file_path):
    """
    Read a string from a text file and return it.

    :param file_path: Path to the text file.
    :return: String read from the text file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

if __name__ == "__main__":
    charsInQR = 200 
    text = read_string_from_file("The Little Prince.txt")
    text = text[:600]
    text = " "*charsInQR*4 + text
    if text:
        text_list = [text[i:i+charsInQR] for i in range(0, len(text), charsInQR)]
        display_qr_codes(text_list)
