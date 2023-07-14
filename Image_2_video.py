import sys
import cv2
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox, QSpinBox

class ImageToVideoConverterGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image to Video Converter')
        self.setFixedSize(300, 350)
        self.setWindowIcon(QIcon('video_tools/trim.png'))
        self.layout = QVBoxLayout()

        background_image = QPixmap('video_tools/pexels-pixabay-257904.jpg').scaled(self.width(), self.height())
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, self.width(), self.height())

        self.label = QLabel('Select image folder:')
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # Align text to center
        self.label.setStyleSheet("color: white;")
        self.layout.addWidget(self.label)

        self.button = QPushButton('Browse')
        self.button.clicked.connect(self.selectImageFolder)
        self.layout.addWidget(self.button)

        self.fps_label = QLabel('FPS:')
        self.fps_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fps_label.setStyleSheet("color: white;")
        self.layout.addWidget(self.fps_label)

        self.fps_spinbox = QSpinBox()
        self.fps_spinbox.setRange(1, 60)  # Set the range for fps values
        self.fps_spinbox.setValue(24)  # Set the default value
        self.layout.addWidget(self.fps_spinbox)

        self.setLayout(self.layout)
        self.show()

    def selectImageFolder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Image Folder')
        if folder:
            self.image_folder = folder
            self.convertImagesToVideo()

    def convertImagesToVideo(self):
        output_path, _ = QFileDialog.getSaveFileName(self, 'Save Video', '', 'MP4 Files (*.mp4)')

        if output_path:
            self.hide()  # Hide the main window during processing

            self.processing_message = QMessageBox(self)
            self.processing_message.setWindowTitle('Processing')
            self.processing_message.setIcon(QMessageBox.Information)
            self.processing_message.setText('Converting images to video...')
            self.processing_message.setStandardButtons(QMessageBox.NoButton)
            self.processing_message.show()

            QtCore.QCoreApplication.processEvents()  # Process pending events to show the processing message

            fps = self.fps_spinbox.value()  # Get the selected fps value

            image_files = sorted([f for f in os.listdir(self.image_folder) if f.endswith('.jpg') or f.endswith('.png')])

            frame = cv2.imread(os.path.join(self.image_folder, image_files[0]))
            height, width, channels = frame.shape

            video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

            for image_file in image_files:
                image_path = os.path.join(self.image_folder, image_file)
                frame = cv2.imread(image_path)

                video_writer.write(frame)

            video_writer.release()

            self.processing_message.hide() 
            self.show()  

            QMessageBox.information(self, 'Task Complete', f"Video created: {output_path}", QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageToVideoConverterGUI()
    sys.exit(app.exec_())
