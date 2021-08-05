# Generated by Django 3.0 on 2021-07-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_auto_20210721_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itemlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('iimage', models.ImageField(default='ics.jpg', upload_to='itemimages/')),
                ('itavailability', models.CharField(choices=[('available', 'AV'), ('not available', 'NA')], default='none', max_length=20)),
            ],
        ),
    ]