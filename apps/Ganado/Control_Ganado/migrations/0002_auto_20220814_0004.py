# Generated by Django 3.2.7 on 2022-08-14 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Control_Ganado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Padre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ganado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ganado_padre', to='Control_Ganado.ganado')),
            ],
        ),
        migrations.CreateModel(
            name='Madre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ganado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ganado_madre', to='Control_Ganado.ganado')),
            ],
        ),
        migrations.AlterField(
            model_name='ganado',
            name='madre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='madre_ganado', to='Control_Ganado.madre'),
        ),
        migrations.AlterField(
            model_name='ganado',
            name='padre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='padre_ganado', to='Control_Ganado.padre'),
        ),
    ]