from .database.DB import DB


class Warehouse(DB):
    """
    Класс для работы со складом
    """

    TABLE = 'warehouse'

    def add_new_product_to_warehouse(self, product_id):
        """
        Добавить новый товар на склад
        :param product_id:
        :return:
        """
        try:
            product_id = int(product_id)
            self.cursor.execute(
                "INSERT INTO {} (product_id, quantity) VALUES (%s, 0)".format(self.TABLE),
                [product_id]
            )
            self.conn.commit()
        except Exception as exc:
            exit('Ошибка записи: {}'.format(exc))

    def update_product_quantity(self, product_id, quantity):
        """
        Изменить кол-во товара
        :param product_id:
        :param quantity:
        :return:
        """
        try:
            product_id = int(product_id)
            self.cursor.execute(
                "UPDATE {} SET quantity = %s WHERE product_id = {};".format(self.TABLE, product_id),
                [quantity]
            )
            self.conn.commit()
        except Exception as exc:
            exit('Ошибка обновления: {}'.format(exc))








