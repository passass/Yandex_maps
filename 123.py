import sys
import requests
from os import remove

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap


# Унаследуем наш класс от простейшего графического примитива QWidget
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def getImage(self):
        lon = 37.530887
        lat = 55.703118
        delta = 0.002

        paramsz = {'ll': ','.join([str(lon), str(lat)]), 'spn': ','.join([str(delta), str(delta)]), 'l': 'map'}

        map_request = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_request, params=paramsz)

        if not response:
            print('Ошибка обработки запроса')
            print('Введены неправильные аргументы')
            return False

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        return True

    def initUI(self):
        self.setFixedSize(600, 600)
        self.setWindowTitle('Яндекс карты')

        if self.getImage():
            self.pixmap = QPixmap(self.map_file)
            self.image = QLabel(self)
            self.image.move(0, 0)
            self.image.resize(600, 600)
            self.image.setPixmap(self.pixmap)

            remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
