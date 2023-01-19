'''
Management-команда на добавление пользователей в базу данных из csv файла.
'''

import csv

from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Загрузка пользователей в базу из файла csv.'

    def handle(self, *args, **options):
        with open('static/data/users.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            users = []
            for row in csv_reader:
                try:
                    create_users = User(
                        id=int(row[0]),
                        username=row[1],
                        email=row[2],
                        role=row[3],
                        bio=row[4],
                        first_name=row[5],
                        last_name=row[6]
                    )
                    users.append(create_users)
                except ValueError:
                    print('Несоответствие данных игнорировано.')
            User.objects.bulk_create(users)
