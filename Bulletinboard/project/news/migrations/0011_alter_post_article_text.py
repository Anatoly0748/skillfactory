# Generated by Django 4.1.5 on 2023-05-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_reply_remove_category_subscribers_remove_post_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='article_text',
            field=models.TextField(),
        ),
    ]
