# Generated by Django 4.0.1 on 2022-09-09 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawel_pedryc_developer', '0009_essaycls_organizer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='essaycls',
            name='organizer_email',
        ),
    ]
