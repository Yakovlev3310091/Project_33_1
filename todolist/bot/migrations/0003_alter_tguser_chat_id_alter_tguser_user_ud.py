# Generated by Django 4.0.1 on 2022-12-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_tguser_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='chat_id',
            field=models.IntegerField(verbose_name='id чата'),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='user_ud',
            field=models.IntegerField(verbose_name='id пользователя'),
        ),
    ]
