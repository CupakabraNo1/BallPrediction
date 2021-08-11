import cv2
import csv
import torch
import os

from argparse import ArgumentParser
from constants import DEFAULT_HEADER, VALUES_PATH

# model = torch.load("workspace/model/best.pt")

def get_ball_coordinates(frame):

    # calculations for center of the object detected on frame

    x, y = 1, 1

    return x, y


def video_ball_detection(path_to_file):
    video = cv2.VideoCapture(path_to_file)
    frame_number = 1

    value_matrix = []

    while True:
        success, frame = video.read()
        if not success:
            break

        x, y = get_ball_coordinates(frame)
        if not x or not y:
            frame_number += 1
            continue

        value_matrix.append([frame_number, x, y])

        # cv2.imwrite("data/frame-{}.jpg".format(frame_number), frame)

        frame_number += 1

    video.release()
    return value_matrix


if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("video", type=str, help="Path to video file")
    argument_parser.add_argument("visualize", type=bool, help="Enable visualization")
    arguments = argument_parser.parse_args()

    video_file = arguments.video
    visualization = arguments.visualize

    print("Starting recognition process...")

    matrix = video_ball_detection(video_file)

    with open(VALUES_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(DEFAULT_HEADER)
        writer.writerows(matrix)
    print("Recognition process ended.")

    if visualization:
        print("Starting visualization...")
        visualization_command = "python workspace\show_ball_dataset.py {} {}".format(video_file, VALUES_PATH)
        os.system(visualization_command)

    cv2.destroyAllWindows()