# Generated by Django 3.1.7 on 2021-03-24 04:12

import corps.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corp',
            fields=[
                ('corp_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('corp_name', models.CharField(max_length=50)),
            ],
            managers=[
                ('objects', corps.managers.CustomModelManager()),
            ],
        ),
    ]