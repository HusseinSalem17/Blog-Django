# Generated by Django 5.0 on 2023-12-06 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookStore', '0002_tag_order_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='bookStore.tag'),
        ),
    ]
