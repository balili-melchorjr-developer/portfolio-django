# Generated by Django 5.0.2 on 2024-02-27 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_technology_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='technology',
            field=models.ManyToManyField(blank=True, null=True, to='api.technology'),
        ),
    ]