# Generated by Django 4.0.1 on 2022-09-09 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawel_pedryc_developer', '0005_sendmemessage_essaycls_guest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='essaycls',
            old_name='prog_lang',
            new_name='language',
        ),
    ]