# run_movenet

## Build OpenCV


### cmake param
```shell
# configure
cmake -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules ^
    -D WITH_GSTREAMER=ON ^
    -D CMAKE_BUILD_TYPE=Release ^
    -D BUILD_opencv_python3=ON ^
    -D BUILD_opencv_python_bindings_generator=ON ^
    -D BUILD_opencv_python_tests=ON ^
    -D OPENCV_FORCE_PYTHON_LIBS=ON ^
    -D PYTHON3_NUMPY_INCLUDE_DIRS="F:/uv_test/run_movenet/.venv/Lib/site-packages/numpy/_core/include" ^
    -D PYTHON3_PACKAGES_PATH="F:/uv_test/run_movenet/.venv/Lib/site-packages" ^
    -D BUILD_NEW_PYTHON_SUPPORT=ON ^
    -D PYTHON_EXECUTABLE="C:/Users/ikeko/AppData/Roaming/uv/python/cpython-3.10.18-windows-x86_64-none/python.exe" ^
    -D PYTHON_INCLUDE_DIR="C:/Users/ikeko/AppData/Roaming/uv/python/cpython-3.10.18-windows-x86_64-none/include" ^
    -D PYTHON_LIBRARY="C:/Users/ikeko/AppData/Roaming/uv/python/cpython-3.10.18-windows-x86_64-none/libs/python310.lib" ^
    -D BUILD_SHARED_LIBS=ON ^
    -D WITH_FFMPEG=OFF ^
    -D GSTREAMER_app_LIBRARY="C:/1.0/msvc_x86_64/lib/gstapp-1.0.lib" ^
    -D GSTREAMER_audio_LIBRARY="C:/1.0/msvc_x86_64/lib/gstaudio-1.0.lib" ^
    -D GSTREAMER_base_LIBRARY="C:/1.0/msvc_x86_64/lib/gstbase-1.0.lib" ^
    -D GSTREAMER_glib_INCLUDE_DIR="C:/1.0/msvc_x86_64/include/glib-2.0" ^
    -D GSTREAMER_glib_LIBRARY="C:/1.0/msvc_x86_64/lib/glib-2.0.lib" ^
    -D GSTREAMER_glibconfig_INCLUDE_DIR="C:/1.0/msvc_x86_64/lib/glib-2.0/include" ^
    -D GSTREAMER_gobject_LIBRARY="C:/1.0/msvc_x86_64/lib/gobject-2.0.lib" ^
    -D GSTREAMER_gst_INCLUDE_DIR="C:/1.0/msvc_x86_64/include/gstreamer-1.0" ^
    -D GSTREAMER_gstreamer_LIBRARY="C:/1.0/msvc_x86_64/lib/gstreamer-1.0.lib" ^
    -D GSTREAMER_pbutils_LIBRARY="C:/1.0/msvc_x86_64/lib/gstpbutils-1.0.lib" ^
    -D GSTREAMER_riff_LIBRARY="C:/1.0/msvc_x86_64/lib/gstriff-1.0.lib" ^
    -D GSTREAMER_video_LIBRARY="C:/1.0/msvc_x86_64/lib/gstvideo-1.0.lib" ^
    ../../opencv

# build
cmake --build . --config Release -- /m:8

#install 
cmake --build . --config Release --target install

```