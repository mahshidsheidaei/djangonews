# Generated by Django 4.2.1 on 2023-07-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category_img/'),
        ),
    ]
