# Generated by Django 2.2.4 on 2019-08-12 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=49)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=156)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('departament', models.ForeignKey(blank=True, default='TBD', null=True, on_delete=False, to='coreManagerEmployees.Departament')),
            ],
        ),
    ]
