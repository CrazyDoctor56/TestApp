from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
                              QHBoxLayout, QMessageBox, QRadioButton)

from PyQt6.QtCore import Qt

app = QApplication([])
win = QWidget()

win.setWindowTitle("Ochko indusa")
win.resize(600, 400)

question = QLabel("Який третій президент України")

answer_1 = QRadioButton("Кравчук")
answer_2 = QRadioButton("Кучма")
answer_3 = QRadioButton("Порошенко")
answer_4 = QRadioButton("Ющенко")

main_layout = QVBoxLayout()

main_layout.addWidget(question, alignment = Qt.AlignmentFlag.AlignCenter)

h_line_1 = QHBoxLayout()
h_line_2 = QHBoxLayout()

h_line_1.addWidget(answer_1, alignment = Qt.AlignmentFlag.AlignCenter)
h_line_1.addWidget(answer_2, alignment = Qt.AlignmentFlag.AlignCenter)
h_line_2.addWidget(answer_3, alignment = Qt.AlignmentFlag.AlignCenter)
h_line_2.addWidget(answer_4, alignment = Qt.AlignmentFlag.AlignCenter)

main_layout.addLayout(h_line_1)
main_layout.addLayout(h_line_2)

def show_winer():
    message_box = QMessageBox()
    message_box.setText("Молодець! Ти виграв 10 логіків")
    message_box.exec()

def show_lose():
    message_box = QMessageBox()
    message_box.setText("Шкода, але ти не виграв 10 логіків")
    message_box.exec()

answer_1.clicked.connect(show_lose)
answer_2.clicked.connect(show_lose)
answer_3.clicked.connect(show_lose)
answer_4.clicked.connect(show_winer)













win.setLayout(main_layout)
win.show()
app.exec()