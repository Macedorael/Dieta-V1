# Generated by Django 4.2.3 on 2023-07-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dietas_app", "0003_alimento_refeicao_medida_dietas"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dietas",
            name="quantidade",
            field=models.IntegerField(max_length=20, verbose_name="Quantidade"),
        ),
    ]
