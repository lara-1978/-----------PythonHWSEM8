# Задача 3. Агрегирование данных из CSV файла
# Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV файл.
# JSON файл содержит данные о продуктах (название, цена, количество на складе).
# В CSV файле каждая строка должна соответствовать одному продукту.
# Пример: Из файла products.json нужно создать products.csv

import json
import csv


def json_to_csv(json_file, csv_file):
    """Превращает данные из JSON файла в CSV файл."""
# Чтение данных из JSON файла
    with open(json_file, 'r') as f:
        data = json.load(f)
#  Запись данных в CSV файл
    with open(csv_file, 'w', newline='') as f:
        fieldnames = data[0].keys()

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()  # Запись заголовков
        writer.writerows(data)

if __name__ =='__main__':
    json_to_csv('products.json', 'products.csv')





