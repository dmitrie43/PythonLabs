import configparser
import psycopg2


class DB:
    """Класс для работы с бд postgresql"""

    conn = False
    cursor = False
    PATH_TO_CONFIG = 'D:\PythonWorks\Labs\Lab3-6\config\db.ini'

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(self.PATH_TO_CONFIG)
        try:
            conn = psycopg2.connect(
                dbname=config['DB']['dbname'],
                user=config['DB']['username'],
                password=config['DB']['password'],
                host=config['DB']['host'],
                port=config['DB']['port']
            )
            cursor = conn.cursor()
            setattr(self, 'cursor', cursor)
            setattr(self, 'conn', conn)
        except psycopg2.Error as exc:
            exit('Проблема с подключением: {}'.format(exc))

    def __del__(self):
        del self.cursor
