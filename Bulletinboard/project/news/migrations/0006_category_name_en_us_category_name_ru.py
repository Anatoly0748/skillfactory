# Generated by Django 4.1.5 on 2023-04-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_category_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en_us',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]