# Generated by Django 3.2.13 on 2022-06-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0004_alter_livro_data_cadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
