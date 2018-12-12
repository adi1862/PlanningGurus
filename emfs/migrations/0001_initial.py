# Generated by Django 2.0.7 on 2018-12-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True)),
                ('city', models.CharField(max_length=25)),
                ('region', models.CharField(max_length=25)),
                ('email', models.EmailField(blank=True, max_length=25, unique=True)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('events', models.CharField(choices=[('BR', 'Birthday'), ('WD', 'Wedding'), ('DW', 'DWedding'), ('AN', 'Anniversary'), ('FS', 'Festive'), ('SP', 'Special')], default='BR', max_length=2)),
            ],
        ),
    ]
