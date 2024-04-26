import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QFileDialog
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Отправка файла по ссылке")

        self.layout = QVBoxLayout()

        self.lbl_link = QLabel("Ссылка:")
        self.layout.addWidget(self.lbl_link)

        self.txt_link = QLineEdit()
        self.layout.addWidget(self.txt_link)

        self.lbl_file_path = QLabel("Путь к файлу:")
        self.layout.addWidget(self.lbl_file_path)

        self.txt_file_path = QLineEdit()
        self.layout.addWidget(self.txt_file_path)

        self.btn_browse_file = QPushButton("Выбрать файл")
        self.btn_browse_file.clicked.connect(self.browse_file)
        self.layout.addWidget(self.btn_browse_file)

        self.btn_send = QPushButton("Отправить файл")
        self.btn_send.clicked.connect(self.send_file)
        self.layout.addWidget(self.btn_send)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл")
        if file_path:
            self.txt_file_path.setText(file_path)

    def send_file(self):
        link = self.txt_link.text()
        file_path = self.txt_file_path.text()

        if link and file_path:
            try:
                with open(file_path, 'rb') as file:
                    files = {'file': file}
                    response = requests.post(link, files=files)
                    if response.status_code == 200:
                        print("Файл успешно отправлен!")
                    else:
                        print("Произошла ошибка при отправке файла.")
            except Exception as e:
                print("Ошибка:", e)
        else:
            print("Введите ссылку и путь к файлу перед отправкой.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())