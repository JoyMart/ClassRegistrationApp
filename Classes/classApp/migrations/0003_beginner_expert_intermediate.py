# Generated by Django 3.1.1 on 2020-09-22 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0002_auto_20200922_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='beginner',
            fields=[
                ('djangoclasses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='classApp.djangoclasses')),
            ],
            bases=('classApp.djangoclasses',),
        ),
        migrations.CreateModel(
            name='expert',
            fields=[
                ('djangoclasses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='classApp.djangoclasses')),
            ],
            bases=('classApp.djangoclasses',),
        ),
        migrations.CreateModel(
            name='intermediate',
            fields=[
                ('djangoclasses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='classApp.djangoclasses')),
            ],
            bases=('classApp.djangoclasses',),
        ),
    ]
