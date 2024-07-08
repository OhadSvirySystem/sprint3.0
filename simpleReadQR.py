import cv2
from pyzbar.pyzbar import decode
import argparse

def decode_qr_code(frame):
    """
    Decode QR codes in the given frame and return the decoded text.
    """
    decoded_objects = decode(frame)
    texts = []
    for obj in decoded_objects:
        texts.append(obj.data.decode("utf-8"))
    return texts

def process_video(file_path):
    """
    Process the video file to extract and print text from QR codes.
    """
    cap = cv2.VideoCapture(file_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file {file_path}")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        texts = decode_qr_code(frame)
        for text in texts:
            print("Decoded Text:", text)

        cv2.imshow('Video Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process video to extract text from QR codes.")
    parser.add_argument('file_path', type=str, help='Path to the video file.')
    args = parser.parse_args()
    process_video(args.file_path)
