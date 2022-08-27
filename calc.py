# import sys
#
# from PyQt5.QtWidgets import (
#     QApplication,
#     QWidget,
#     QLabel,
#     QPushButton,
#     QLineEdit,
#     QComboBox,
#     QRadioButton,
#     QHBoxLayout,
#     QVBoxLayout,
#     QGridLayout,
#     QFormLayout,
#     QDialog,
#     QDialogButtonBox,
#     QMainWindow,
#     QToolBar,
#     QStatusBar,
# )
#
#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Hello world')
# window.setGeometry(50, 50, 300, 300)
#
# message = QLabel('<h1>Hello world</h1>', parent=window)
# message.move(50, 50)
#
# button = QPushButton('click', parent=window)
# button.move(50, 100)
#
# edit = QLineEdit('', parent=window)
# edit.move(50, 150)
#
# combo = QComboBox(parent=window)
# combo.addItems(['python', 'java', 'go', 'java script'])
# combo.move(200, 50)
#
# radio = QRadioButton('python', parent=window)
# radio.move(200, 150)
#
#
# window.show()
#
# sys.exit(app.exec_())

# 1. Horizontal  Vertical Layout
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Vertical')
#
# # layout = QHBoxLayout()
# layout = QVBoxLayout()
#
# layout.addWidget(QPushButton('top', parent=window))
# layout.addWidget(QPushButton('center', parent=window))
# layout.addWidget(QPushButton('bottom', parent=window))
# layout.addWidget(QLabel('Bye-bye', parent=window))
#
# window.setLayout(layout)
#
# window.show()
#
# sys.exit(app.exec_())

# Grid layout

# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Grid')
#
# layout = QGridLayout()
#
# layout.addWidget(QPushButton('button'), 0, 0)
# layout.addWidget(QPushButton('button'), 0, 1)
# layout.addWidget(QPushButton('button'), 0, 2)
# layout.addWidget(QPushButton('button'), 1, 0)
# layout.addWidget(QPushButton('button'), 1, 1)
# layout.addWidget(QPushButton('button'), 1, 2)
# layout.addWidget(QPushButton('button'), 2, 0)
# layout.addWidget(QPushButton('button'), 2, 1, 1, 2)
#
# window.setLayout(layout)
#
# window.show()
#
# sys.exit(app.exec_())

# Form layout
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Form')
#
# layout = QFormLayout()
#
# layout.addRow('Name', QLineEdit())
# layout.addRow('Age', QLineEdit())
# layout.addRow('Education', QLineEdit())
# layout.addRow('Job', QLineEdit())
# layout.addRow('Hobbies', QLineEdit())
# layout.addWidget(QPushButton('Submit'))
#
# window.setLayout(layout)
#
# window.show()
#
# sys.exit(app.exec_())

# Dialog window


# class Dialog(QDialog):
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.setWindowTitle('Dialog window')
#         box_layout = QVBoxLayout()
#         form_layout = QFormLayout()
#
#         form_layout.addRow('Name', QLineEdit())
#         form_layout.addRow('Age', QLineEdit())
#         form_layout.addRow('Education', QLineEdit())
#         form_layout.addRow('Job', QLineEdit())
#         form_layout.addRow('Hobbies', QLineEdit())
#
#         box_layout.addLayout(form_layout)
#
#         buttons = QDialogButtonBox()
#
#         buttons.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
#
#         box_layout.addWidget(buttons)
#
#         self.setLayout(box_layout)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dialog = Dialog()
#     dialog.show()
#     sys.exit(app.exec_())
#
#
# class MyWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle('My Window')
#         self.setCentralWidget(QLabel('Central title'))
#         self._create_menu()
#         self._create_tool_bar()
#         self._create_status_bar()
#
#     def _create_menu(self):
#         self.menu = self.menuBar().addMenu('Menu')
#         self.menu.addMenu('Edit')
#         self.menu.addAction('Exit', self.close)
#         self.menu.addAction('Hello', self.adjustSize)
#
#     def _create_tool_bar(self):
#         tools = QToolBar()
#         self.addToolBar(tools)
#         tools.addAction('Exit', self.close)
#
#     def _create_status_bar(self):
#         status = QStatusBar()
#         status.showMessage('Some message')
#         self.setStatusBar(status)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.setGeometry(50, 50, 300, 300)
#     window.show()
#     sys.exit(app.exec_())

# Signals
# def greeting():
#     if mes.text():
#         mes.setText('')
#     else:
#         mes.setText('Hello')
#
#
# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle('Signals')
#
# layout = QVBoxLayout()
# button = QPushButton('Greet')
#
# button.clicked.connect(greeting)
#
# layout.addWidget(button)
# mes = QLabel('')
# layout.addWidget(mes)
#
# window.setLayout(layout)
#
# window.show()
# sys.exit(app.exec_())
###############################################################################
import sys
from functools import partial

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QGridLayout,
    QPushButton
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


ERROR = 'Error'


class Calculator(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(500, 500)
        self.general_layout = QVBoxLayout()

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)
        # Створюємо дісплей калькулятора
        self._create_display()
        # Створюємо віджети кнопок
        self._create_buttons()

    def _create_display(self):
        """ Calculator display. """
        self.display = QLineEdit()
        self.display.setFixedHeight(150)
        self.display.setAlignment(Qt.AlignLeft)
        self.display.setReadOnly(True)
        self.display.setFont(QFont('Times', 32))

        self.general_layout.addWidget(self.display)

    def _create_buttons(self):
        self.buttons = {}
        buttons_layout = QGridLayout()
        buttons = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            'C': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '=': (3, 4),
        }
        for button_text, position in buttons.items():
            self.buttons[button_text] = QPushButton(button_text)
            self.buttons[button_text].setFixedSize(80, 80)
            self.buttons[button_text].setFont(QFont('Times', 18))
            buttons_layout.addWidget(
                self.buttons[button_text], position[0], position[1]
            )

        self.general_layout.addLayout(buttons_layout)

    def set_display_text(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        return self.display.text()

    def clear_display(self):
        self.set_display_text('')


class CalculatorController:

    def __init__(self, window, function):
        self._window = window
        self._evaluate = function

        self._connect_signals()

    def _build_expression(self, symbol):
        if self._window.display_text() == ERROR:
            self._window.clear_display()

        expression = self._window.display_text() + symbol
        self._window.set_display_text(expression)

    def _connect_signals(self):
        for button_text, button in self._window.buttons.items():
            if button_text not in {'=', 'C'}:
                button.clicked.connect(
                    partial(self._build_expression, button_text)
                )
        self._window.buttons['='].clicked.connect(self._calculate_result)
        self._window.display.returnPressed.connect(self._calculate_result)
        self._window.buttons['C'].clicked.connect(self._window.clear_display)

    def _calculate_result(self):
        result = self._evaluate(expression=self._window.display_text())
        self._window.set_display_text(result)


def evaluate_expression(expression):
    try:
        result = str(eval(expression))
    except Exception:
        result = ERROR

    return result


def main():
    calculator = QApplication(sys.argv)
    window = Calculator()
    window.show()
    CalculatorController(window=window, function=evaluate_expression)
    sys.exit(calculator.exec_())


if __name__ == '__main__':
    main()
