# Generated by Django 4.2.5 on 2023-10-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautySalon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='specialization',
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/services/<django.db.models.fields.CharField>', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='master',
            name='specialization',
            field=models.ManyToManyField(to='beautySalon.specialization', verbose_name='Специализации'),
        ),
    ]
