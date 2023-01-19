'''
Management-команда на добавление отзывов в базу данных из csv файла.
'''

import csv

from django.core.management.base import BaseCommand
from reviews.models import Review


class Command(BaseCommand):
    help = 'Загрузка отзывов в базу из файла csv.'

    def handle(self, *args, **options):
        with open('static/data/review.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            reviews = []
            for row in csv_reader:
                try:
                    create_reviews = Review(
                        id=int(row[0]),
                        title_id=int(row[1]),
                        text=row[2],
                        author_id=int(row[3]),
                        score=int(row[4]),
                        pub_date=row[5]
                    )
                    reviews.append(create_reviews)
                except ValueError:
                    print('Несоответствие данных игнорировано.')
            Review.objects.bulk_create(reviews)
