# Generated by Django 4.2 on 2023-06-12 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_picture', models.ImageField(upload_to='images/')),
            ],
        ),
    ]