# Generated by Django 4.0.1 on 2022-09-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel_pedryc_developer', '0006_rename_prog_lang_essaycls_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='essaycls',
            name='date',
            field=models.DateField(default='2022-09-09'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='essaycls',
            name='organizer_email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
    ]
