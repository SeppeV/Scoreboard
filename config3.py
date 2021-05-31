import configparser

from PySide6 import QtWidgets

app = QtWidgets.QApplication()

wid = QtWidgets.QWidget()
wid.show()


# ...
layout = QtWidgets.QFormLayout(wid) # Nieuw Grid -> Form

label = QtWidgets.QLabel("Titel:")
edit = QtWidgets.QTextEdit()
layout.addRow(label, edit)  # Nieuw

label = QtWidgets.QLabel("TeamA logo:")
edit = QtWidgets.QTextEdit()
layout.addRow(label, edit) # Nieuw

label = QtWidgets.QLabel("TeamB logo:")
edit = QtWidgets.QTextEdit()
layout.addRow(label, edit)  # Nieuw

label = QtWidgets.QLabel("Team A:")
edit = QtWidgets.QTextEdit()
layout.addRow(label, edit) # Nieuw

label = QtWidgets.QLabel("Team B:")
edit = QtWidgets.QTextEdit()
layout.addRow(label, edit) # Nieuw



app.exec_()



