import cv2
import numpy as np


def detect_screen_boundaries(frame):
    # Convert the frame to HSV (hue, saturation, value) color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range for green color in HSV
    lower_green = np.array([0, 70, 50])
    upper_green = np.array([10, 255, 255])

    # Create a mask that captures areas with the green color
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Assuming the largest contour corresponds to the screen
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        return x, y, w, h
    else:
        return None


def crop_video(input_path, output_path):
    # Open the input video
    cap = cv2.VideoCapture(input_path)

    # Read the first frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to read the video")
        return

    # Detect screen boundaries
    screen_rect = detect_screen_boundaries(frame)
    if screen_rect is None:
        print("No green screen found in the first frame")
        return

    x, y, w, h = screen_rect

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (w, h))

    # Loop through the video frames
    while ret:
        # Crop the frame
        cropped_frame = frame[y:y + h, x:x + w]

        # Write the cropped frame to the output video
        out.write(cropped_frame)

        # Read the next frame
        ret, frame = cap.read()

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved to {output_path}")


