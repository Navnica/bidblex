# Generated by Django 5.0.6 on 2024-05-14 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_certificate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='certificate',
            new_name='certificate_url',
        ),
    ]
