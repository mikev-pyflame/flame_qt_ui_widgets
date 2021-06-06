class FlameLineEditFileBrowse(QtWidgets.QLineEdit):
    """
    Custom Qt Flame Clickable Line Edit Widget with File Browser

    To use:

    lineedit = FlameLineEditFileBrowse('some_path', 'Python (*.py)', window)

    file_path: Path browser will open to. If set to root folder (/), browser will open to user home directory
    filter_type: Type of file browser will filter_type for. If set to 'dir', browser will select directory
    """

    clicked = QtCore.Signal()

    def __init__(self, file_path, filter_type, parent, *args, **kwargs):
        super(FlameLineEditFileBrowse, self).__init__(*args, **kwargs)

        self.filter_type = filter_type
        self.file_path = file_path

        self.setText(file_path)
        self.setParent(parent)
        self.setMinimumHeight(28)
        self.setReadOnly(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clicked.connect(self.file_browse)
        self.setStyleSheet('QLineEdit {color: #898989; background-color: #373e47; font: 14px "Discreet"}'
                           'QLineEdit:disabled {color: #6a6a6a; background-color: #373737}')

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.setStyleSheet('QLineEdit {color: #bbbbbb; background-color: #474e58; font: 14px "Discreet"}'
                               'QLineEdit:disabled {color: #6a6a6a; background-color: #373737}')
            self.clicked.emit()
            self.setStyleSheet('QLineEdit {color: #898989; background-color: #373e47; font: 14px "Discreet"}'
                               'QLineEdit:disabled {color: #6a6a6a; background-color: #373737}')
        else:
            super().mousePressEvent(event)

    def file_browse(self):
        from PySide2 import QtWidgets

        file_browser = QtWidgets.QFileDialog()

        # If no path go to user home directory

        if self.file_path == '/':
            self.file_path = os.path.expanduser("~")
        if os.path.isfile(self.file_path):
            self.file_path = self.file_path.rsplit('/', 1)[0]

        file_browser.setDirectory(self.file_path)

        # If filter_type set to dir, open Directory Browser, if anything else, open File Browser

        if self.filter_type == 'dir':
            file_browser.setFileMode(QtWidgets.QFileDialog.Directory)
            if file_browser.exec_():
                self.setText(file_browser.selectedFiles()[0])
        else:
            file_browser.setFileMode(QtWidgets.QFileDialog.ExistingFile) # Change to ExistingFiles to capture many files
            file_browser.setNameFilter(self.filter_type)
            if file_browser.exec_():
                self.setText(file_browser.selectedFiles()[0])
