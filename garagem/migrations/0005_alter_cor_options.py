# Generated by Django 4.2.1 on 2023-05-09 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0004_alter_veiculo_categoria_alter_veiculo_cor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name': 'Cor', 'verbose_name_plural': 'Cors'},
        ),
    ]
