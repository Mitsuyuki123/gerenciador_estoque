# Generated by Django 5.0.6 on 2024-07-13 05:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_ativo', models.BooleanField(default=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(blank=True, default='', max_length=255)),
            ],
            options={
                'verbose_name': 'usuário',
                'verbose_name_plural': 'usuários',
                'db_table': 'usuario',
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True)),
                ('preco', models.CharField(blank=True, max_length=50)),
                ('quantidade', models.IntegerField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('imagem', models.TextField(blank=True, null=True)),
                ('thumbnail', models.TextField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
                'db_table': 'produto',
                'ordering': ['nome'],
            },
        ),
    ]