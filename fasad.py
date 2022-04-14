import logging

from data_base import Database


class facade:
    """
    Класс фасада
    """
    def __init__(self, name='KosoyGpaph.db'):
        """
        создание объекта базы данных, структуры данных.
        Gpaph_wait_for_save - False, если нет данных для сохранения, True, если есть данные для сохранения
        :param name: имя базы данных
        """

        self.DB = Database(name)


    def build_kosoy(self):
        """
        запись элементов из БД в структуру данных
        :return: None
        """
        Gpaph = self.DB.get_from_db()
        if Gpaph != []:
            for a in Gpaph:
                self.graph

    def insert_value(self, key, Gpaph):
        """
        Вставка элементов в структуру данных
        :param key: ключ для вставки
        :param Graph: данные для вставки
        :return: None
        """
        self.Gpaph_wait_for_save = True
        self.graph.insert(key, Gpaph)

    def delete_value(self, key):
        """
        Удаление данных из структуры данных
        :param key: ключ, по которому нужно найти объект и удалить его
        :return: None
        """
        self.Gpaph_wait_for_save = True
        self.graph= self.graph.delete(key)

    def save_data(self):
        """
        Если есть несохраненные данные (Gpaph_wait_for_save==True), тогда в БД записываются новые данные
        :return: None
        НУЖНО
        """
        if self.Gpaph_wait_for_save:
            self.Gpaph_wait_for_save = False
            path = self.graph
            path.pop(0)
            self.DB.save_all(path)
            logging.log(logging.INFO, ' данные добавлены в бд')
        else:
            logging.log(logging.INFO, ' нет несохраненных данных')
