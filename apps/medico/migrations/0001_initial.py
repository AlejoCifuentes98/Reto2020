# Generated by Django 3.2.8 on 2021-10-18 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remisiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medico', models.CharField(max_length=50)),
                ('descripción', models.TextField()),
                ('atencion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.atencionmedica')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripción', models.TextField(max_length=500)),
                ('atencion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pacientes.atencionmedica')),
            ],
        ),
    ]
