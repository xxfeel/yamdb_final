'''
Management-команда на добавление коментариев
к отзывам в базу данных из csv файла.
'''

import csv

from django.core.management.base import BaseCommand
from reviews.models import Comment


class Command(BaseCommand):
    help = 'Загрузка комментарие в базу из файла csv.'

    def handle(self, *args, **options):
        with open(
            'static/data/comments.csv', 'r', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            comments = []
            for row in csv_reader:
                try:
                    create_comments = Comment(
                        id=int(row[0]),
                        review_id=int(row[1]),
                        text=row[2],
                        author_id=int(row[3]),
                        pub_date=row[4]
                    )
                    comments.append(create_comments)
                except ValueError:
                    print('Несоответствие данных игнорировано.')
            Comment.objects.bulk_create(comments)
