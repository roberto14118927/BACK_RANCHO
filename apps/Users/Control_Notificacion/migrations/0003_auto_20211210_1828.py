# Generated by Django 3.2.7 on 2021-12-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control_Notificacion', '0002_control_notificacion_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='control_notificacion',
            name='fecha',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='control_notificacion',
            name='hora',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
