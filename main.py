from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLineEdit,
    QLabel)


app = QApplication([])
window = QWidget()
window.setStyleSheet("background:black;border:1px dashed white")
layout = QVBoxLayout()
label = QLabel('Вклад')
layout.addWidget(label)



def rt(input_a, input_b, input_c, layout):
    a = int(input_a.text())
    b = int(input_b.text())
    c = int(input_c.text())
    b = b/100 + 1
    for i in range(c):
        a *= b
    rts = str(a)
    rt2 = rts.find('.')
    result = "Итог: " + rts[0:rt2+3]
    label = QLabel(result)
    label.setStyleSheet("color:green;font-size:30px")
    layout.addWidget(label)
    input_a.hide()
    input_b.hide()
    input_c.hide()
    dtd.hide()
    xnono.hide()
    window.setStyleSheet("background:black")





xnono = QLabel("КАлькулятор вклада")
xnono.setStyleSheet("color:green;font-size:30px")
layout.addWidget(xnono)

input_a = QLineEdit()
input_a.setPlaceholderText("Введте сумму вклад:")
input_a.setStyleSheet("color:blue;font-size:30px")
layout.addWidget(input_a)

input_b = QLineEdit()
input_b.setPlaceholderText("Введите процент вклада:")
input_b.setStyleSheet("color:blue;font-size:30px")
layout.addWidget(input_b)

input_c = QLineEdit()
input_c.setPlaceholderText("Введите кол лет:")
input_c.setStyleSheet("color:blue;font-size:30px")
layout.addWidget(input_c)

dtd = QPushButton("Ввычислить:")
layout.addWidget(dtd)
dtd.clicked.connect(lambda: rt(input_a, input_b, input_c, layout))
dtd.setStyleSheet("color:blue;font-size:25px")

window.setLayout(layout)
window.resize(400, 200)
window.show()
app.exec_()
