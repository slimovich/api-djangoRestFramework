# Generated by Django 2.2 on 2019-04-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Towns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_code', models.IntegerField()),
                ('region_name', models.CharField(max_length=200)),
                ('dept_code', models.IntegerField()),
                ('distr_code', models.IntegerField()),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('population', models.IntegerField()),
                ('average_age', models.FloatField()),
            ],
        ),
    ]
