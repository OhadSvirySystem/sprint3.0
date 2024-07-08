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
    for index, text in enumerate(text_list):
        generate_qr_code(text, index)
        img = cv2.imread(f'qr_code_{index}.png')

        # Create a fullscreen window
        cv2.namedWindow('QR Code', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('QR Code', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        cv2.imshow('QR Code', img)
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
def display_colored_screen(time,color = (0, 0, 255)):
    """
    Display a red screen using OpenCV.
    """
    # Create a red screen
    red_screen = np.zeros((1080, 1920, 3), np.uint8)
    red_screen[:] = color

    # Create a fullscreen window
    cv2.namedWindow('Red Screen', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Red Screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow('Red Screen', red_screen)
    cv2.waitKey(time)  # Display the red screen for 3 seconds

    cv2.destroyAllWindows()
if __name__ == "__main__":
    charsInQR = 100 
    text = read_string_from_file("omri1.txt")
    if text:
        text_list = [text[i:i+charsInQR] for i in range(0, len(text), charsInQR)]
        display_colored_screen(2000,(0, 255, 0))
        display_qr_codes(text_list)
