# Generated by Django 5.0.2 on 2024-02-27 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_category_options_alter_city_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='image',
            field=models.ImageField(default='images/18961868.jpg', upload_to='images/'),
        ),
    ]
