# Generated by Django 3.0 on 2021-07-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_additem_itimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additem',
            name='itimg',
            field=models.ImageField(default='ics.jpg', upload_to='itemimages/'),
        ),
    ]