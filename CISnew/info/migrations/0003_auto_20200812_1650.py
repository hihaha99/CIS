# Generated by Django 3.0.3 on 2020-08-12 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20200812_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stores',
            old_name='days',
            new_name='day',
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('day', models.CharField(default='nil', max_length=200)),
                ('start_hour', models.TimeField(default='08:00:00')),
                ('end_hour', models.TimeField(default='08:00:00')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Stores')),
            ],
        ),
    ]