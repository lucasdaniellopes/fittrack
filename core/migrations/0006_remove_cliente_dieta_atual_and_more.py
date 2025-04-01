# Generated by Django 5.1.7 on 2025-04-01 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_perfil_cliente_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='dieta_atual',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='treino_atual',
        ),
        migrations.AddField(
            model_name='dieta',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dietas', to='core.cliente'),
        ),
        migrations.AddField(
            model_name='treino',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treinos', to='core.cliente'),
        ),
    ]
