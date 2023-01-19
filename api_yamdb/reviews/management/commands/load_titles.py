'''
Management-команда на добавление произведений в базу данных из csv файла.
'''

import csv

from django.core.management.base import BaseCommand
from reviews.models import Title


class Command(BaseCommand):
    help = 'Загрузка произведений в базу из файла csv.'

    def handle(self, *args, **options):
        with open('static/data/titles.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            titles = []
            for row in csv_reader:
                try:
                    create_titles = Title(
                        id=int(row[0]),
                        name=row[1],
                        year=row[2],
                        category_id=int(row[3])
                    )
                    titles.append(create_titles)
                except ValueError:
                    print('Несоответствие данных игнорировано.')
            Title.objects.bulk_create(titles)
