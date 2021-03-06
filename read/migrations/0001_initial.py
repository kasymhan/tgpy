# Generated by Django 2.1.5 on 2019-02-02 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAbiturient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enlisted', models.BooleanField()),
                ('abiturient', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='read.BlogAbiturient')),
            ],
        ),
        migrations.CreateModel(
            name='BlogArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogCountr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogFacully',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogSpecial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out', models.IntegerField()),
                ('fac', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='read.BlogFacully')),
            ],
        ),
        migrations.AddField(
            model_name='blogapplication',
            name='special',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='read.BlogSpecial'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='read.BlogArea'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='read.BlogCity'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='read.BlogCountr'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='read.BlogRegion'),
        ),
    ]
