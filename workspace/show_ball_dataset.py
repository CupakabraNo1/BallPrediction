""" Visualize ball labels on a video frame """

from argparse import ArgumentParser
import numpy as np
import pandas as pd
import cv2


if __name__ == "__main__":
    """Here we define the argumnets for the script."""
    arg_parser = ArgumentParser()
    arg_parser.add_argument("video", type=str, help="Path to video file")
    arg_parser.add_argument("labels", type=str, help="Path to csv with ball positions")
    args = arg_parser.parse_args()

    video_file = args.video
    labels_file = args.labels

    # Read labels file: should have header
    # [frame_no,ball_x,ball_y] :: frame number, ball x coord in pixels, ball y coord in pixels
    df_frames = pd.read_csv(labels_file)
    df_frames.set_index("frame_no", inplace=True)

    # Load video
    cap = cv2.VideoCapture(video_file)

    # Get number of frames in video
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Visualize k random frames
    for frame_no in np.random.randint(0, num_frames, 100000):

        # Some frames don't have the ball or it is occluded
        if frame_no not in df_frames.index:
            continue

        # Get frame labels for that frame number
        frame_info = df_frames.loc[frame_no]

        # Go to frame_no in video
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)

        # Read frame
        ret, frame = cap.read()

        # Get pos
        ball_pos = np.array([frame_info["ball_x"], frame_info["ball_y"]]).astype(np.int)

        # Drawing points
        pt1, pt2 = tuple(ball_pos - 5), tuple(ball_pos + 5)

        # Draw green rectangle on frame
        cv2.rectangle(frame, pt1, pt2, (0, 255, 0), thickness=2)

        # Resize frame for visualization (original is 1080p_
        show_img = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # Show frame with ball coordinate
        cv2.imshow("Frame", show_img)
        if cv2.waitKey(0) & 0xFF == ord("q"):
            break
