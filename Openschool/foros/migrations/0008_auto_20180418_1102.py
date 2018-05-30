# Generated by Django 2.0.3 on 2018-04-18 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foros', '0007_auto_20180411_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='Estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='Fecha_Publicacion',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
