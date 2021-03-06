# Generated by Django 2.2 on 2019-10-17 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=300)),
                ('foto', models.ImageField(default=None, upload_to='')),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Novedades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=45)),
                ('cuerpo', models.CharField(max_length=100)),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('valor', models.IntegerField()),
                ('color', models.IntegerField(choices=[(1, 'Rojo'), (2, 'Azul'), (3, 'Amarillo'), (4, 'Verde'), (5, 'Blanco'), (6, 'Negro'), (7, 'Otro')])),
                ('tipo', models.IntegerField(choices=[(1, 'Crop Top'), (2, 'Gorro'), (3, 'Bufanda'), (4, 'Otro')])),
                ('stock', models.IntegerField()),
                ('foto', models.ImageField(default=None, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('contraseña', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=45)),
                ('ciudad', models.CharField(max_length=45)),
                ('precio', models.IntegerField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='app.Carro')),
            ],
        ),
        migrations.AddField(
            model_name='carro',
            name='contexto',
            field=models.ManyToManyField(to='app.Productos'),
        ),
    ]
