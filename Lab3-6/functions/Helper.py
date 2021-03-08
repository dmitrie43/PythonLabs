import os
import csv


class Helper:
    """
    Класс для требований к программе. Лаб 3
    Дополнительный функционал
    """

    @staticmethod
    def get_count_in_dir(path) -> list:
        """
        Возвращает кол-во файлов в директории
        :param str path:
        :return list:
        """

        return os.listdir(path)

    @staticmethod
    def get_csv_data(path_to_csv) -> dict:
        """
        Возвращает данные из csv файла
        :param str path_to_csv:
        :except OSError:
        :return dict:
        """

        data = dict()
        try:
            with open(path_to_csv, "r") as file_obj:
                reader = csv.reader(file_obj)
                for index, row in enumerate(reader):
                    data[index] = row
        except OSError:
            print('Ошибка работы с файлом')

        return data

    @staticmethod
    def record_in_csv(path_to_csv, csv_data):
        """
        Запись данных в csv файл
        :param str path_to_csv:
        :param list csv_data:
        :except Exception:
        :return void:
        """

        try:
            with open(path_to_csv, "a", newline='') as file_obj:
                writer = csv.writer(file_obj, delimiter=',')
                for line in csv_data:
                    writer.writerow(line)
        except Exception:
            print('Ошибка работы с файлом')

"""Пусть дана некоторая директория (папка). Посчитайте количество файлов в данной директории (папке) и выведите на экран"""
path_to_dir = os.getcwd()
# print(Helper.get_count_in_dir(path_to_dir))

"""Считайте информацию из файла в соответствующую структуру (словарь)"""
path_to_file = 'D:\PythonWorks\Labs\Lab3-6\\files\data.csv'
# print(Helper.get_csv_data(path_to_file))

"""Выведите информацию об объектах, отсортировав их по одному полю (строковому)"""
print(sorted(Helper.get_csv_data(path_to_file).items(), key=lambda item: item[1]))

"""Выведите информацию об объектах, отсортировав их по одному полю (числовому)"""
print(sorted(Helper.get_csv_data(path_to_file).items()))

"""Выведите информацию, соответствующую какому-либо критерию"""
print(Helper.get_csv_data(path_to_file))
data = Helper.get_csv_data(path_to_file).items()
res3 = {k: v for k, v in data if 'leff' in v}
print(res3)

"""Добавьте к программе возможность сохранения новых данных обратно в файл."""
# data = ['tv,skyline3,20,22000'.split(',')]
# Helper.record_in_csv(path_to_file, data)


