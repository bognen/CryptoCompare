# Generated by Django 2.2.12 on 2020-05-13 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocloud', '0008_auto_20200512_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloudcontract',
            name='coin',
        ),
        migrations.AddField(
            model_name='cloudcontract',
            name='coin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cryptocloud.Coin'),
        ),
        migrations.RemoveField(
            model_name='cloudcontract',
            name='company',
        ),
        migrations.AddField(
            model_name='cloudcontract',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cryptocloud.CloudCompany'),
        ),
    ]
