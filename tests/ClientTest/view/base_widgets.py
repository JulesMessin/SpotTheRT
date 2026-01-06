from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QPixmap

class BackgroundWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image = QPixmap(image_path)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def paintEvent(self, event):
        painter = QPainter(self)
        if not self.image.isNull():
            painter.drawPixmap(self.rect(), self.image)
        else:
            # Fond gris par défaut si l'image n'est pas trouvée
            painter.fillRect(self.rect(), self.palette().window())