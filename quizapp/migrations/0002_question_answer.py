# Generated by Django 3.1.3 on 2021-01-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.IntegerField(default=0),
        ),
    ]