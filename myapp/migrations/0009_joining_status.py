# Generated by Django 2.0.1 on 2019-09-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_joining'),
    ]

    operations = [
        migrations.AddField(
            model_name='joining',
            name='status',
            field=models.CharField(default='none', max_length=25),
            preserve_default=False,
        ),
    ]