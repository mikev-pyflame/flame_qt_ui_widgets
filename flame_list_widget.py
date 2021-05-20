class FlameListWidget(QtWidgets.QListWidget):
    """
    Custom Qt Flame List Widget

    To use:

    list_widget = FlameListWidget(window)
    """

    def __init__(self, parent_window, *args, **kwargs):
        super(FlameListWidget, self).__init__(*args, **kwargs)

        self.setMinimumSize(300, 250)
        self.setParent(parent_window)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setAlternatingRowColors(True)
        self.setStyleSheet('QListWidget {color: #9a9a9a; background-color: #2a2a2a; alternate-background-color: #2d2d2d; outline: none; font: 14px "Discreet"}'
                           'QListWidget::item:selected {color: #d9d9d9; background-color: #474747}')