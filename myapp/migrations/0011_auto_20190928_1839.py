# Generated by Django 2.0.1 on 2019-09-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20190926_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joining',
            name='status',
            field=models.CharField(max_length=25),
        ),
    ]