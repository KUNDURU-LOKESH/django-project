# Generated by Django 3.0 on 2021-07-20 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_auto_20210718_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='additem',
            name='itimg',
            field=models.ImageField(default='ics.jfif', upload_to='itemimages/'),
        ),
    ]
