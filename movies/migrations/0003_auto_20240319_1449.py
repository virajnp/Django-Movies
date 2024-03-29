# Generated by Django 2.1 on 2024-03-19 19:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movies_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('numbers_in_stock', models.IntegerField()),
                ('daily_rate', models.FloatField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Genre')),
            ],
        ),
        migrations.RemoveField(
            model_name='movies',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
    ]
