# Generated by Django 5.0.6 on 2024-05-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_certificate_product_certificate_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='certificate_url',
            field=models.FileField(upload_to='store/static/docs'),
        ),
    ]
