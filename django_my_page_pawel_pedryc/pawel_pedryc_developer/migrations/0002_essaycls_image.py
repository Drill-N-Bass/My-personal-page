# Generated by Django 4.0.1 on 2022-09-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel_pedryc_developer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='essaycls',
            name='image',
            field=models.ImageField(default='test image', upload_to='images'),
            preserve_default=False,
        ),
    ]