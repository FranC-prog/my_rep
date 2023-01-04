# Generated by Django 4.1.4 on 2023-01-03 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_rename_user_avatar_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaDeJuegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('juegosDeEmpresa', models.CharField(max_length=100)),
                ('paisOrigen', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=400)),
                ('resena', models.CharField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='JugadoresProfesionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tag', models.CharField(max_length=50)),
                ('juego', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
