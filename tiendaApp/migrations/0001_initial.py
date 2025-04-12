# Generated by Django 4.2.4 on 2023-11-14 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Precio', models.IntegerField()),
                ('Descripción', models.CharField(max_length=100)),
                ('Stock', models.IntegerField()),
                ('Link', models.CharField(max_length=100)),
                ('Tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('Correo', models.CharField(max_length=30)),
                ('Contraseña', models.CharField(max_length=20)),
                ('Teléfono', models.IntegerField()),
            ],
        ),
    ]
