# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqt_downloader_ui import Ui_Downloader
from huiwan_downloader import HuiWan_Downloader


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Downloader()
        self.ui.setupUi(self)

        self.ui.downloadPBtn.clicked.connect(self.download_start)
        self.ui.downloadPBtn.clicked.connect(self.ui.urlLineText.clear)

    def download_start(self):
        dler = HuiWan_Downloader(self.ui.listTreeWidget, self.get_url())
        dler.start()

    def get_url(self):
        return self.ui.urlLineText.text()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
