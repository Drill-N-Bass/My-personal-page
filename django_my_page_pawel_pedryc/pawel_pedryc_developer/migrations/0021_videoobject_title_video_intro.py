# Generated by Django 4.1.1 on 2023-02-14 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel_pedryc_developer', '0020_alter_videoobject_title_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoobject',
            name='title_video_intro',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]