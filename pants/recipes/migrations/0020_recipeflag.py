# Generated by Django 3.0.2 on 2020-03-10 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0019_recipetag_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char', models.SlugField(max_length=1, unique=True)),
                ('name', models.SlugField(max_length=20, unique=True)),
                ('description', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]
