import sys, pickle, logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTabWidget, QWidget, QListWidgetItem
from ui_py.ui_mainWindow import Ui_MainWindow
from ui_py.ui_settings import Ui_tabWidget
from ui_py.ui_about import Ui_Form
from main import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

        prefs = self.read_prefs()

        self.file = file_processor()
        self.settings = SettingsWindow()

        # Connection of buttons
        self.ui.convertButton.clicked.connect(self.file.send_to_main)
        self.ui.clearButton.clicked.connect(self.clear_qlistwidget)

        self.ui.actionPrefences.triggered.connect(self.open_settings)
        self.ui.actionAbout_2VTT.triggered.connect(self.open_about)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for path in (event.mimeData().urls()):
            if self.file.check_everything(path.toLocalFile()):
                self.file.add_path(path.toLocalFile())

    def clear_qlistwidget(self):
        self.file.path_list = []
        self.ui.fileList.clear()


    def open_settings(self):
        self.prefences = SettingsWindow()
        self.prefences.show()

    def open_about(self):
        self.about = aboutWindow()
        self.about.show()

    def read_prefs(self):
        try:
            with open('prefences.dat', 'rb') as file:
                return pickle.load(file)

        except FileNotFoundError:
            with open('prefences.dat', 'wb') as file:
                default = {'logging': True}
                pickle.dump(default, file)
            
class file_processor:
    """
    Processes files user adds to the programm
    """

    path_list = []
    _supported_formats = ['srt']
    filew = file_worker()

    def __init__(self):
        self.read_prefs()

    def add_path(self, path):
        self.path_list.append(path)
        file = path.split('/').pop()
        self.refresh_list(file)

    def refresh_list(self, file):
        item = QListWidgetItem(file)
        MainWindow.ui.fileList.addItem(item)

    def send_to_main(self, path):
        for path in self.path_list:
            name = path.split('/').pop().split('.srt')[0]
            self.filew.open_file(path, name)

    def read_prefs(self):
        with open('prefences.dat', 'rb') as file:
            return pickle.load(file)

    def check_everything(self, path):
        if path not in self.path_list and path.split('/').pop().split('.').pop() in self._supported_formats:
            return True
        else:
            return False


class SettingsWindow(QTabWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        self.TabWidget = QTabWidget()
        super(SettingsWindow, self).__init__(parent)
        self.ui_prefs = Ui_tabWidget()
        self.ui_prefs.setupUi(self)

        #This is temperoray, this infromtation 'll parse from file
        self.set_saved_prefences()

        self.ui_prefs.saveButton.clicked.connect(self.save_prefs)


    def save_prefs(self):
        logging_state = self.ui_prefs.checkLogging.isChecked()

        self.prefences_dictionary = {'logging': logging_state}

        self.write_prefs(self.prefences_dictionary)

    def write_prefs(self, data = None):
        with open('prefences.dat', 'wb') as file:
            pickle.dump(data, file)

    def read_prefs(self):
        with open('prefences.dat', 'rb') as file:
            pickle_data = pickle.load(file)

        return pickle_data

    def current_prefs(self):
        return self.prefences_dictionary

    def set_saved_prefences(self):
        prefences_file = self.read_prefs()
        self.ui_prefs.checkLogging.setChecked(prefences_file['logging'])


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