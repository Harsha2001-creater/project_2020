# Generated by Django 3.1.5 on 2021-01-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0004_auto_20210107_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stdquery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
                ('Email', models.EmailField(max_length=254)),
                ('Phonenumber', models.CharField(max_length=20)),
                ('Date', models.CharField(max_length=10)),
            ],
        ),
    ]
