import sys, pickle
#import logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTabWidget, QWidget, QListWidgetItem
from ui_py.ui_mainWindow import Ui_MainWindow
from ui_py.ui_settings import Ui_tabWidget
from ui_py.ui_about import Ui_Form
from processing import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

        self.file = file_processor()
        self.settings = SettingsWindow()

        # Buttoms connection
        self.ui.convertButton.clicked.connect(self.file.send_to_process)
        self.ui.clearButton.clicked.connect(self.clear_qlistwidget)

        self.ui.actionPrefences.triggered.connect(self.open_settings)
        self.ui.actionAbout_2VTT.triggered.connect(self.open_about)

    # Drag&Drop processing
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for path in (event.mimeData().urls()):
            if self.file.check_everything(path.toLocalFile()):
                self.file.add_path(path.toLocalFile())

    # Clear button
    def clear_qlistwidget(self):
        self.file.path_list = []
        self.ui.fileList.clear()


    # Open settings button (cmd + "," on mac)
    def open_settings(self):
        self.prefences = SettingsWindow()
        self.prefences.show()

    # Open about. Didn't test it on win
    def open_about(self):
        self.about = aboutWindow()
        self.about.show()
            
class file_processor:
    """
    Processes files user adds to the programm
    """
    # List with all files you want to convert
    path_list = []
    # List with files program supports
    _supported_formats = ['srt']
    # class from processing.py
    filew = file_worker()
    def add_path(self, path):
        self.path_list.append(path)
        file = path.split('/').pop()
        self.refresh_list(file)

    def refresh_list(self, file):
        item = QListWidgetItem(file)
        MainWindow.ui.fileList.addItem(item)

    def send_to_process(self, path):
        prefs = SettingsWindow.prefs
        for path in self.path_list:
            name = path.split('/').pop().split('.srt')[0]
            self.filew.open_file(path, name, prefs)

    # Check is file format valid
    def check_everything(self, path):
        if path not in self.path_list and path.split('/').pop().split('.').pop() in self._supported_formats:
            return True
        else:
            return False


class SettingsWindow(QTabWidget, Ui_MainWindow):
    # List with settings from file in root
    prefs = {'delete': None}

    def __init__(self, parent=None):
        self.TabWidget = QTabWidget()
        super(SettingsWindow, self).__init__(parent)
        self.ui_prefs = Ui_tabWidget()
        self.ui_prefs.setupUi(self)

        self.set_saved_prefences()
        self.ui_prefs.saveButton.clicked.connect(self.save_prefs)


    def save_prefs(self):
        logging_state = self.ui_prefs.checkDelete.isChecked()
        self.prefences_dictionary = {'delete': logging_state}
        self.write_prefs(self.prefences_dictionary)
        self.read_prefs()

    def write_prefs(self, data = None):
        with open('prefences.dat', 'wb') as file:
            pickle.dump(data, file)

    def set_saved_prefences(self):
        self.read_prefs()
        self.ui_prefs.checkDelete.setChecked(self.prefs['delete'])

    # Get prefs from file in the root dir (not user's root, app root)
    def read_prefs(self):
        try:
            with open('prefences.dat', 'rb') as file:
                delete = pickle.load(file)['delete']

        except FileNotFoundError:
            with open('prefences.dat', 'wb') as file:
                default = {'delete': False}
                pickle.dump(default, file)
                delete = False

        self.prefs['delete'] = delete


class aboutWindow(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(aboutWindow, self).__init__(parent)
        self.ui_prefs = Ui_Form()
        self.ui_prefs.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())