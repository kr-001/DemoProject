# Generated by Django 4.2 on 2023-05-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('work_type', models.CharField(choices=[('YT', 'Youtube'), ('IG', 'Instagram'), ('OT', 'Other')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('work', models.ManyToManyField(related_name='artist', to='app.work')),
            ],
        ),
    ]
