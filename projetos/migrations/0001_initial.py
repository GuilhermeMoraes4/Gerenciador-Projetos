# Generated by Django 5.0.1 on 2024-01-22 16:43

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(default='', max_length=255)),
                ('prioridade', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('acao_no_sprint', models.CharField(default='', max_length=255)),
                ('status', models.CharField(default='', max_length=255)),
                ('area', models.CharField(default='', max_length=255)),
                ('tipo_de_projeto', models.CharField(default='', max_length=255)),
                ('horas_estimadas', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('data_inicio', models.DateField(default=django.utils.timezone.now)),
                ('prazo', models.DateField(default=django.utils.timezone.now)),
                ('observacao', models.CharField(default='', max_length=255)),
                ('proprietario', models.CharField(default='', max_length=255)),
                ('custo', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
