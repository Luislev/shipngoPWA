# Generated by Django 3.1.3 on 2023-06-28 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20230622_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='yappy_number',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]