import sys
import os
# Gstreamer plugin path
os.add_dll_directory('F:/uv_test/run_movenet/module/opencv/build/bin/Release')
os.add_dll_directory("C:/1.0/msvc_x86_64/bin")
import cv2
import numpy as np



def main():
    print(cv2.getBuildInformation())


if __name__ == "__main__":
    main()
