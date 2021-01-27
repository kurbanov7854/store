# Generated by Django 3.1.5 on 2021-01-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]