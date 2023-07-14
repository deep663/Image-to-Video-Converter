# Image to Video Converter

The Image to Video Converte is an application that allows you to convert a folder of images into a video file. The GUI provides a user-friendly interface to select the image folder, set the frames per second (FPS) for the video, and specify the output path for the video file.

## Features

- Select an image folder: Browse and select the folder containing the images you want to convert to a video.
- Set the FPS: Specify the frames per second (FPS) for the resulting video.
- Save the video: Choose the output path and file name for the converted video.
- Visual feedback: The GUI provides a background image and a processing message to indicate the progress of the conversion process.

## Prerequisites

- Python 3.10
- PyQt5
- OpenCV (cv2)

## Installation

1. Clone the repository or download the source code files.
2. Install the required dependencies using pip:
```shell
pip install pyqt5 opencv-python
```

## Usage

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the following command to start the application:
```shell
python image_to_video_converter.py
```
3. The GUI window will appear. Click the "Browse" button and select the image folder you want to convert.
4. Set the desired FPS value using the spinner control.
5. Click the "Convert" button.
6. Choose the output path and file name for the video file and click "Save".
7. The conversion process will start, and a processing message will be displayed.
8. Once the conversion is complete, a message box will appear indicating the successful creation of the video file.
9. Click "OK" to close the message box and continue using the application.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This application was created using the PyQt5 library and OpenCV. Special thanks to the developers and contributors of these libraries for their valuable work.

Feel free to customize the README.md file according to your project's specific requirements and add any additional sections or information you deem necessary.
