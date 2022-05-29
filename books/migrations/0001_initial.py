# Generated by Django 4.0.4 on 2022-05-28 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=50)),
                ('published_year', models.IntegerField()),
                ('acquired', models.BooleanField(default=False)),
                ('thumbnail', models.URLField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorBookRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
    ]