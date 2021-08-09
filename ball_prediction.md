### Soccer ball position prediction in frames

Objective is to learn an algorithm that will predict the ball coordinate in the image given a video/frame.  In addition to evaluating the efficiency and performance of your technical approach, we also give marks for simplicity, engineering craftsmanship, and maintainability.


Final evaluation script: Write a script that will take a file path of a 1080p video as input argument and will:
1. write a csv file with the header `frame_no,ball_x,ball_y` and the rows representing the predicted ball coordinates for all the frames where a ball has been detected. (as `part1.csv`)
2. visualize frame by frame detections (as `show_ball_dataset.py` but visualizing consecutive frame predictions). This feature should be enabled/disabled based on a argument to the script.

#### Recommended:
The code should be uploaded on Github repo with play/install instructions in order to be evaluated.

#### Dataset available `part1.mp4` video with 27k frames labeled in `part1.csv`. You can use `show_ball_dataset.py` to view random frames and the ball labels.

#### Suggested tools (but not limited to): Python, Opencv, PyTorch

#### Relaxed problem:
- No need to worry about live-detection (but decent detection time / frame would be appreciated)
- No need to do detection on the full img (1080p); you can scale it down
- It's ok if you don't detect where the ball is not there. (you can always predict a ball coordinate)
- Liberty in choosing the algorithms used/ preprocessing of the images.
- The test video is from the same game so the requirement for generalization is pretty low.