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
                ('abiturient', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='write.BlogAbiturient')),
            ],
        ),
        migrations.CreateModel(
            name='BlogArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogCountr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogFacully',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogSpecial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('fac', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='write.BlogFacully')),
            ],
        ),
        migrations.AddField(
            model_name='blogapplication',
            name='special',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='write.BlogSpecial'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='write.BlogArea'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='write.BlogCity'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='write.BlogCountr'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='write.BlogRegion'),
        ),
    ]
