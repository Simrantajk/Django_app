# Generated by Django 5.0.6 on 2024-06-30 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('scheme_id', models.AutoField(primary_key=True, serialize=False)),
                ('scheme', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(default='ISE', max_length=3)),
                ('scheme', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sgpacalc.scheme')),
            ],
        ),
        migrations.CreateModel(
            name='Sem',
            fields=[
                ('sem_id', models.AutoField(primary_key=True, serialize=False)),
                ('sem', models.IntegerField()),
                ('branch', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sgpacalc.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_code', models.CharField(max_length=255)),
                ('sub_name', models.CharField(max_length=255)),
                ('credits', models.IntegerField()),
                ('max_marks', models.IntegerField()),
                ('sem', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sgpacalc.sem')),
            ],
        ),
    ]
