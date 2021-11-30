# Generated by Django 3.2.9 on 2021-11-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('offer', models.IntegerField()),
                ('category_id', models.IntegerField()),
            ],
        ),
    ]
