import os

import cv2


def select_bounding_boxes(frame):
    print("Select 4 bounding boxes. Press ENTER after selecting each box and then ESC to finish.")
    boxes = cv2.selectROIs("Select Bounding Boxes", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()
    return boxes


def main():
    directory = "data"
    videos = [f for f in os.listdir(directory) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

    if not videos:
        print("No video files found in the directory.")

    first_video_path = os.path.join(directory, videos[0])
    cap = cv2.VideoCapture(first_video_path)

    if not cap.isOpened():
        print(f"Unable to open video: {first_video_path}")
        return

    ret, frame = cap.read()
    if not ret:
        print("Unable to read the first frame of the video.")
        cap.release()
        return

    # Select bounding boxes on the first frame
    bounding_boxes = select_bounding_boxes(frame)
    print(bounding_boxes)


if __name__ == "__main__":
    main()
