# Generated by Django 3.1.7 on 2021-05-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210518_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('method', models.CharField(choices=[('online', 'online'), ('cod', 'cod')], default='cod', max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[('yes', 'y'), ('no', 'n')], default='cod', max_length=100, null=True),
        ),
    ]
