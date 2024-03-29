# Generated by Django 4.1.5 on 2023-05-09 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0009_remove_postcategory_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('time_in', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='subscribers',
        ),
        migrations.RemoveField(
            model_name='post',
            name='rating',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
