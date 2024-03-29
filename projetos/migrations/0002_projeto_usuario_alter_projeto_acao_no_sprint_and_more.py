# Generated by Django 5.0.1 on 2024-01-22 17:04

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projeto',
            name='acao_no_sprint',
            field=models.CharField(default='', max_length=255, verbose_name='Ação no Sprint'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='area',
            field=models.CharField(default='', max_length=255, verbose_name='Área'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='custo',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Custo Estimado'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='data_inicio',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Início'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='horas_estimadas',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Horas Estimadas'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='observacao',
            field=models.CharField(default='', max_length=255, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='prazo',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Prazo de Conclusão'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='prioridade',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Prioridade'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='proprietario',
            field=models.CharField(default='', max_length=255, verbose_name='Proprietário do Projeto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='status',
            field=models.CharField(default='', max_length=255, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='tipo_de_projeto',
            field=models.CharField(default='', max_length=255, verbose_name='Tipo do Projeto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='titulo',
            field=models.CharField(default='', max_length=255, verbose_name='Título'),
        ),
    ]
