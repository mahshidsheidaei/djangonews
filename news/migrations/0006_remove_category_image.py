# Generated by Django 4.2.1 on 2023-07-16 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
