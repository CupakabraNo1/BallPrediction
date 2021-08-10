# imports
import cv2

from argparse import ArgumentParser
from PIL import Image


def detect_ball(image):
    return ''


def get_ball_coordinates(frame):
    image = Image.fromarray(frame)

    detection = detect_ball(image)

    return 1, 1


def video_ball_detection(path_to_file):
    video = cv2.VideoCapture(path_to_file)
    frame_number = 0

    success = True
    while success:
        success, frame = video.read()
        x, y = get_ball_coordinates(frame)

        if not x or not y:
            frame_number += 1
            continue
        print("{}, {}, {}".format(frame_number, x, y))
        frame_number += 1
    video.release()


if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("video", type=str, help="Path to video file")
    argument_parser.add_argument("visualize", type=bool, help="Enable visualization")
    arguments = argument_parser.parse_args()

    print(arguments)
    video_file = arguments.video
    visualization = arguments.visualize

    video_ball_detection(video_file)

    cv2.destroyAllWindows()