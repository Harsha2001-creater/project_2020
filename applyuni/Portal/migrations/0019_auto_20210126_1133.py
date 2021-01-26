# Generated by Django 3.1.5 on 2021-01-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0018_auto_20210125_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='univdetail',
            name='Amount1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Approvalauthority',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Courseapproval',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Coursename',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Coursetype',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Criteria1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Criteria2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Criteria3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Duration1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Facultyname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Noofsems',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Sem1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Sem2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Sem3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Sem4',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Sem5',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Sem6',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='univdetail',
            name='Tutionfee',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
