# Generated by Django 3.2.9 on 2021-11-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='q_type',
        ),
        migrations.AddField(
            model_name='questions',
            name='one_answer',
            field=models.BooleanField(default=1),
        ),
    ]
