# Generated by Django 3.1.3 on 2020-12-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20201204_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
