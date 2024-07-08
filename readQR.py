import cv2
from pyzbar.pyzbar import decode

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
    Process the video file to extract and print unique text from QR codes in order.
    """
    cap = cv2.VideoCapture(file_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {file_path}")
        return

    seen_texts = set()
    ordered_texts = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        texts = decode_qr_code(frame)
        for text in texts:
            if text not in seen_texts:
                seen_texts.add(text)
                ordered_texts.append(text)

        cv2.imshow('Video Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Print unique decoded texts in the order they appeared
    print("Unique decoded texts in order:")
    for text in ordered_texts:
        print(text)

if __name__ == "__main__":
    video_file_path = "littlePrinceQR.mp4"  # Replace with your video file path
    process_video(video_file_path)
