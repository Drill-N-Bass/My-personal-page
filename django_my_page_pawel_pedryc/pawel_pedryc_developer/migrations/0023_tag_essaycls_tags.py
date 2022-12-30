# Generated by Django 4.1.1 on 2022-12-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel_pedryc_developer', '0022_alter_essaycls_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='essaycls',
            name='tags',
            field=models.ManyToManyField(to='pawel_pedryc_developer.tag'),
        ),
    ]