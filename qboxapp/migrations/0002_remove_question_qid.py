# Generated by Django 4.1.3 on 2022-12-05 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qboxapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='qid',
        ),
    ]
