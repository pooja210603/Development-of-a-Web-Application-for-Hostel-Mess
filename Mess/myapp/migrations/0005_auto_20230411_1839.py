# Generated by Django 3.2.16 on 2023-04-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_menuitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='description',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='name',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='price',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='b_foodlist',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='b_ingredients',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='d_foodlist',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='d_ingredients',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='l_foodlist',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='l_ingredients',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='s_foodlist',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='s_ingredients',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]
