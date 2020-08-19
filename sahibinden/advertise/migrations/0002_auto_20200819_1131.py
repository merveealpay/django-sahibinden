# Generated by Django 2.2.13 on 2020-08-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExteriorFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Frontal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='InteriorFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Landscape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SuitableForDisabled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='advertise',
            name='exterior_feature',
            field=models.ManyToManyField(to='advertise.ExteriorFeature'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='frontal',
            field=models.ManyToManyField(to='advertise.Frontal'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='interior_feature',
            field=models.ManyToManyField(to='advertise.InteriorFeature'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='landscape',
            field=models.ManyToManyField(to='advertise.Landscape'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='locality',
            field=models.ManyToManyField(to='advertise.Locality'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='suitable_for_disabled',
            field=models.ManyToManyField(to='advertise.SuitableForDisabled'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='transportation',
            field=models.ManyToManyField(to='advertise.Transportation'),
        ),
    ]
