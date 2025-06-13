# Generated by Django 5.2.1 on 2025-06-04 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_categoria_produto_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numero_cartao', models.CharField(max_length=16)),
                ('validade', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=4)),
                ('data_compra', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produto')),
            ],
        ),
    ]
