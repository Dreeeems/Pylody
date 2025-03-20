import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton,QFileDialog,QVBoxLayout,QWidget
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Pylody')
        self.setGeometry(100,100,400,300)

        self.player =  QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.initUi()

    def initUi(self):
        layout = QVBoxLayout()

        self.btn_open = QPushButton("Open file")
        self.btn_open.clicked.connect(self.openFile)
        layout.addWidget(self.btn_open)


    

    def openFile(self):
        file_path,_ = QFileDialog.getOpenFileName(self,"Open file","","Audio files (*.mp,*.wav,*.ogg)")
        if file_path:
            self.player.setSource(QUrl.fromLocalFile(file_path))








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec())
 