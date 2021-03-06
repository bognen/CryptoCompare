# Generated by Django 2.2.12 on 2020-05-13 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocloud', '0007_cloudcontract_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloudcontract',
            name='coin',
        ),
        migrations.AddField(
            model_name='cloudcontract',
            name='coin',
            field=models.ManyToManyField(to='cryptocloud.Coin'),
        ),
        migrations.RemoveField(
            model_name='cloudcontract',
            name='company',
        ),
        migrations.AddField(
            model_name='cloudcontract',
            name='company',
            field=models.ManyToManyField(to='cryptocloud.CloudCompany'),
        ),
    ]
