# Generated by Django 2.2.28 on 2023-11-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_auto_20231104_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicletare',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]