# Generated by Django 3.1.2 on 2020-12-27 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='', max_length=15),
        ),
    ]