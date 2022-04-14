import sqlite3
import logging
logging.basicConfig(level=logging.INFO)
# logging.disable(logging.INFO)


class Database:
    """
    класс с функциями дли взаимодействия с базой данных
    """
    def __init__(self, name):
        """
        создает базу данных
        :param name: имя базы данных
        """
        self.db = sqlite3.connect(f"{name}")
        sql = self.db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS Kosoy ( 
            key integer, 
            Gpaph TEXT
        )""")
        self.db.commit()
        sql.close()

    def get_from_db(self):
        """
        Возвращает все значения из базы данных в переменной Gpaph
        :return: Gpaph
        """
        sql = self.db.cursor()
        Gpaph = [value for value in sql.execute(f"SELECT * FROM Kosoy")]
        if not Gpaph:
            logging.log(logging.INFO, ' база данных пуста')
        sql.close()
        return Gpaph

    def del_all(self):
        """
        Вспомогательная функция для save_all.
        Удаляет все данные в базе данных.
        :return: None
        """
        cur = self.db.cursor()
        cur.execute("DELETE from Kosoy")
        self.db.commit()

    def db_insert(self, key, Gpaph):
        """
        функция для вставки данных в базу данных
        :param key: ключ, который вставляем в базу данных
        :param Gpaph: данные, которые вставляем в базу данных
        :return: None
        """
        cur = self.db.cursor()
        cur.execute("INSERT INTO Kosoy VALUES (?,?)", (key, Gpaph))
        self.db.commit()
        cur.close()

    def save_all(self, path):
        """
        Переписывает все старые данные на новые - удаляет данные и записывает текущие
        :param path: путь обхода структуры данных
        :return: None
        """
        self.del_all()
        for val in path:
            if val[1] is not None:
                self.db_insert(val[0], val[1])
