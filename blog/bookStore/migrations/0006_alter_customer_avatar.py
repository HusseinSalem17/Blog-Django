# Generated by Django 5.0 on 2023-12-10 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookStore', '0005_customer_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, default='person.jpg', null=True, upload_to=''),
        ),
    ]