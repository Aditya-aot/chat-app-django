# Generated by Django 3.0.7 on 2020-09-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20200923_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
