# Generated by Django 3.1.4 on 2021-01-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0020_auto_20210129_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Univeristyname', models.CharField(max_length=500)),
                ('About', models.CharField(max_length=500)),
            ],
        ),
    ]
