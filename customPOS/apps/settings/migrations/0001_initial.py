# Generated by Django 4.0.3 on 2022-06-24 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('url_save', 'url_save')], max_length=50, unique=True)),
                ('text_value', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
