# Generated by Django 3.2.8 on 2021-10-15 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoFamiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('identificacion', models.IntegerField(unique=True)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=80, unique=True)),
                ('fecha_nacimineto', models.DateField()),
                ('grupo_familiar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.grupofamiliar')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('identificacion', models.IntegerField(unique=True)),
                ('correo', models.EmailField(max_length=80, unique=True)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.especialidad')),
            ],
        ),
        migrations.AddField(
            model_name='grupofamiliar',
            name='medico_cabecera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.medico'),
        ),
    ]
