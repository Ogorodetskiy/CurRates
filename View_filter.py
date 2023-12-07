from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QTableView, QWidget, QHBoxLayout, QVBoxLayout, QHeaderView, QLabel, QLineEdit
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery
import program_parameters as pp

class TableView(QWidget):
    def __init__(self):
        super().__init__()

        # создаем модель таблицы
        self.model = QSqlTableModel(self)

        # соединяемся с базой данных (тут пример для SQLite)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(pp.db_path)
        if not db.open():
            print("Cannot open database")
            exit(1)

        # устанавливаем модель таблицы и заполняем ее данными
        self.model.setTable("countries")
        self.model.select()

        # создаем виджеты для отображения таблицы и фильтр
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.filterLabel = QLabel("Фильтр:")
        self.filterLineEdit = QLineEdit()
        self.filterLineEdit.textChanged.connect(self.filterChanged)

        # компоновка элементов окна
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.filterLabel)
        hbox.addWidget(self.filterLineEdit)
        vbox.addLayout(hbox)
        vbox.addWidget(self.tableView)
        self.setLayout(vbox)

        # задаем свойства окна
        self.setWindowTitle("Окно с таблицей и фильтром")
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def filterChanged(self, text):
        # устанавливаем фильтр по введенному тексту
        self.model.setFilter(f"name LIKE '%{text}%'")
        self.model.select()

if __name__ == '__main__':
    app = QApplication([])
    tv = TableView()
    app.exec()