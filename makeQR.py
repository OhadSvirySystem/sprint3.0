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
        cv2.imshow('QR Code', img)
        cv2.waitKey(1000)  # Display each QR code for 1 second
    cv2.destroyAllWindows()

if __name__ == "__main__":
    text_list = [
        "Ensure proper lighting and a stable video feed to maximize the accuracy of QR code detection.Adjust the display duration (cv2.waitKey(1000)) and capture frame rate as needed based on the performance of your setup.You may want to implement additional error handling and synchronization mechanisms for ",
        "חכמנלחגמנךלזחמהנךלחבזמהנףזמסהנדםןגעחמנםזןגעצמפצגזמע,פדגעמפםהנחד",
        "Transfer text using QR codes.",
        "OpenAI GPT-4",
        "End of messages."
    ]
    display_qr_codes(text_list)
