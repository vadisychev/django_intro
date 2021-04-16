# Generated by Django 3.1.7 on 2021-03-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='user_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='user_surname',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_email',
            field=models.EmailField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
