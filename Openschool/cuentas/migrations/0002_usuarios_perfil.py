# Generated by Django 2.0.3 on 2018-04-04 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='perfil',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
