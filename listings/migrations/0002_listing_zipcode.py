# Generated by Django 3.2 on 2021-05-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(default=True, max_length=4),
            preserve_default=False,
        ),
    ]
