# Generated by Django 3.1.5 on 2021-01-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0015_auto_20210111_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='temp_pass',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stddetail',
            name='IntDoc',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='stddetail',
            name='SscDoc',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='stddetail',
            name='UniDoc',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='stddetail',
            name='Uploadad',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='stddetail',
            name='Uploadad1',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='stddetail',
            name='Uploadeng',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='stddetail',
            name='Uploadeng1',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='stdquery',
            name='Name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='univdetail',
            name='Applyfee',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
