# Generated by Django 2.0.5 on 2018-05-09 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pdf_articulo', models.FileField(upload_to='documents/')),
                ('Fecha_Publicacion', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('Titulo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Carrera', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario_Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Texto_Respuesta', models.CharField(max_length=200)),
                ('Fecha_Publicacion', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('Articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foros.Articulo')),
                ('Comentarios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foros.Comentario_Articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foros.Carrera')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Materia', models.CharField(max_length=200)),
                ('Carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foros.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Texto_Pregunta', models.CharField(max_length=200)),
                ('Fecha_Publicacion', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('Estado', models.BooleanField(default=False)),
                ('Materia', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='foros.Materia')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta_Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Texto_Respuesta', models.CharField(max_length=200)),
                ('Fecha_Publicacion', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('Comentarios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foros.Respuesta_Pregunta')),
                ('Pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foros.Pregunta')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='Materia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='foros.Materia'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
