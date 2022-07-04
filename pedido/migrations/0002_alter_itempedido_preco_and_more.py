# Generated by Django 4.0.5 on 2022-07-01 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedido',
            name='preco',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='preco_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Promocional'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='variacao',
            field=models.CharField(max_length=255, verbose_name='Variação'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='variacao_id',
            field=models.PositiveIntegerField(verbose_name='Variação Id'),
        ),
    ]