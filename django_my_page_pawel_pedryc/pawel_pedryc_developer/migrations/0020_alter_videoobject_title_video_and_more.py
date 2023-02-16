# Generated by Django 4.1.1 on 2023-02-13 04:07

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pawel_pedryc_developer', '0019_alter_videoobject_video_intro_item_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoobject',
            name='title_video',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='videoobject',
            name='video_item_url',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]