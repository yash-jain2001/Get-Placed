# Generated by Django 3.1 on 2021-07-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210708_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement_company_detail',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
