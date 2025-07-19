import sys
import os
# Gstreamer plugin path
os.add_dll_directory('F:/uv_test/run_movenet/module/opencv/build/bin/Release')
os.add_dll_directory("C:/1.0/msvc_x86_64/bin")
import cv2
import numpy as np



def main():
    cap = cv2.VideoCapture("autovideosrc ! videoconvert ! appsink")
    
    while True:
        cap_available, img_mat = cap.read()
        if not cap_available:
            break
        

        cv2.imshow("img",img_mat)
        
        key = cv2.waitKey(1)
        if key==27: #[esc] key
            break


if __name__ == "__main__":
    main()
