# Generated by Django 4.1.6 on 2023-04-09 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='URL')),
                ('visible', models.BooleanField(verbose_name='¿Visible?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creacion: ')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Actulizacion: ')),
            ],
            options={
                'verbose_name': 'Pagina ',
                'verbose_name_plural': 'Paginas',
            },
        ),
    ]