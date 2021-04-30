class FlameTextEdit(QtWidgets.QTextEdit):
    """
    Custom Qt Flame Text Edit Widget

    To use:

    text_edit = FlameTextEdit('some_text_here', True_or_False, window)
    """

    def __init__(self, text, read_only, parent_window, *args, **kwargs):
        super(FlameTextEdit, self).__init__(*args, **kwargs)

        self.setMinimumHeight(50)
        self.setMinimumWidth(150)
        self.setReadOnly(read_only)
        if read_only:
            self.setStyleSheet('color: #9a9a9a; selection-color: #262626; selection-background-color: #b8b1a7; border: 1px inset #404040; font: 14px "Discreet"')
        else:
            self.setStyleSheet('QTextEdit {color: #9a9a9a; background-color: #373e47; selection-color: #262626; selection-background-color: #b8b1a7; border: 1px inset #404040; font: 14px "Discreet"}'
                               'QTextEdit:focus {background-color: #474e58}')

        self.verticalScrollBar().setStyleSheet('color: #818181; background-color: #313131')
        self.horizontalScrollBar().setStyleSheet('color: #818181; background-color: #313131')
