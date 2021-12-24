from PyQt5.QtWidgets import QWidget, QMenu

class Window(QWidget):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e):
        print(e.globalX(), e.globalY())
        m = QMenu(parent = self)
        m.addAction('Test1')
        m.addAction('text2')
        m.move(e.globalX(), e.globalY())
        m.exec()
