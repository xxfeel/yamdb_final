'''
Management-команда на добавление жанров в базу данных из csv файла.
'''

import csv

from django.core.management.base import BaseCommand
from reviews.models import Genre


class Command(BaseCommand):
    help = 'Загрузка жанров в базу из файла csv.'

    def handle(self, *args, **options):
        with open('static/data/genre.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            genres = []
            for row in csv_reader:
                try:
                    create_genres = Genre(
                        id=int(row[0]),
                        name=row[1],
                        slug=row[2],
                    )
                    genres.append(create_genres)
                except ValueError:
                    print('Несоответствие данных игнорировано.')
            Genre.objects.bulk_create(genres)
