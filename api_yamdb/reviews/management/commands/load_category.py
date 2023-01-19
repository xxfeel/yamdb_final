'''
Management-команда на добавление категорий в базу данных из csv файла.
'''

import csv

from django.core.management.base import BaseCommand
from reviews.models import Category


class Command(BaseCommand):
    help = 'Загрузка категорий в базу из файла csv.'

    def handle(self, *args, **options):
        with open(
            'static/data/category.csv', 'r', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            category = []
            for row in csv_reader:
                try:
                    create_categories = Category(
                        id=int(row[0]),
                        name=row[1],
                        slug=row[2],
                    )
                    category.append(create_categories)
                except ValueError:
                    print('Несоответствие данных игнорировано.')
            Category.objects.bulk_create(category)
