# Generated by Django 4.2.1 on 2023-05-10 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_introduction_remove_user_join_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=1, max_length=20, verbose_name='닉네임'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256, verbose_name='비밀번호'),
        ),
    ]