# Generated by Django 5.0.6 on 2024-05-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_storage_productstorage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(default='', max_length=100),
        ),
    ]