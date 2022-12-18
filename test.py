import cv2
import numpy as np

movie_data="https://github.com/paul-goodall/python_opencv_framedepth/blob/main/test_movie.mov?raw=true"

# print some useful information about a numpy array:
def ndarray_info(nda):
    print("type\t: ", nda.dtype,"\nshape\t: ", nda.shape, "\nmin\t: ", nda.min(), "\nmax\t: ", nda.max(),"\n")

# Get the video frame:
vid_capture = cv2.VideoCapture(movie_data)

# Doesn't seem to watch to change the format:
vid_capture.set(cv2.CAP_PROP_FORMAT, cv2.CV_32F)
print("set? CAP_PROP_FORMAT = " + str(vid_capture.get(cv2.CAP_PROP_FORMAT)))
print("value CV_32F = " + str(cv2.CV_32F))
print("value CV_32FC1 = " + str(cv2.CV_32FC1))
vid_capture.set(cv2.CAP_PROP_FORMAT, 5.0)
print("set? CAP_PROP_FORMAT = " + str(vid_capture.get(cv2.CAP_PROP_FORMAT)))

if (vid_capture.isOpened() == False):
  print("Error opening the video file")
# Read fps and frame count
else:
    vid_fps = vid_capture.get(5)
    vid_frame_count = vid_capture.get(7)
    print('Found ' + movie_data + ' with ' + str(vid_frame_count) + ' frames.')
    while(vid_capture.isOpened()):
        # Try grab+retrieve:
        vid_capture.grab()
        ret1, img1 = vid_capture.retrieve(cv2.CV_32F)
        # Try read:
        ret2, img2 = vid_capture.read()
        if ret1 == True and ret2 == True:
                ndarray_info(img1)
                ndarray_info(img2)
                break
