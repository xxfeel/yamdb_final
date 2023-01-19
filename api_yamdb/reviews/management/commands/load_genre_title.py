'''
Management-команда на добавление жанров и произведений
в промежуточную таблицу из csv файла.
'''

import csv

from django.core.management.base import BaseCommand
from reviews.models import TitleGenre


class Command(BaseCommand):
    help = 'Загрузка жанров и произведений, для manytomany из файла csv.'

    def handle(self, *args, **options):
        with open(
            'static/data/genre_title.csv', 'r', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            genre_title = []
            for row in csv_reader:
                try:
                    create_genres_titles = TitleGenre(
                        id=int(row[0]),
                        title_id=int(row[1]),
                        genre_id=int(row[2]),
                    )
                    genre_title.append(create_genres_titles)
                except ValueError:
                    print('Несоответствие данных игнорировано.')
            TitleGenre.objects.bulk_create(genre_title)
