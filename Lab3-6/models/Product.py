from .database.DB import DB
from .Warehouse import Warehouse


class Product(DB):
    """
    Класс для работы с товароами
    """

    TABLE = 'products'

    def get_all_products(self, with_quantity=False):
        """
        Получить все товары
        :param with_quantity bool
        :return:
        """
        query = "SELECT p.id, p.product_name, p.price, p.article, w.quantity FROM {} AS p".format(self.TABLE)
        if with_quantity:
            query += " LEFT JOIN warehouse AS w ON w.product_id = p.id"

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_new_product(self, product_name, price, article):
        """
        Добавить новый товар
        :param product_name:
        :param price:
        :param article:
        :return:
        """
        try:
            """Ошибка при добавлении записи без id"""
            self.cursor.execute("SELECT MAX(id) FROM {}".format(self.TABLE))
            last_id = self.cursor.fetchone()[0]
            if last_id:
                current_id = last_id + 1
            else:
                current_id = 1
            """"""
            self.cursor.execute(
                "INSERT INTO {} (id, product_name, price, article) VALUES ({}, %s, %s, %s);".format(self.TABLE, current_id),
                [product_name, price, article]
            )
            self.conn.commit()
            warehouse = Warehouse()
            warehouse.add_new_product_to_warehouse(current_id)
        except Exception as exc:
            exit('Ошибка записи: {}'.format(exc))








