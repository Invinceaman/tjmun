# Generated by Django 2.2.3 on 2020-01-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techmun', '0010_auto_20200115_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='commtype',
            name='is_middle',
            field=models.BooleanField(default=False),
        ),
    ]
