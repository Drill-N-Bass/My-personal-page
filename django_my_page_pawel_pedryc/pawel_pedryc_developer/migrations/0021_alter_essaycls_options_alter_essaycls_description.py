# Generated by Django 4.1.1 on 2022-12-13 16:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel_pedryc_developer', '0020_alter_videoobject_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='essaycls',
            options={'verbose_name': 'My Essay'},
        ),
        migrations.AlterField(
            model_name='essaycls',
            name='description',
            field=models.TextField(verbose_name=django.core.validators.MinLengthValidator(10)),
        ),
    ]
