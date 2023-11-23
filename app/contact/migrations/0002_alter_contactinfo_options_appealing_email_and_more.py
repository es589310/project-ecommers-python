# Generated by Django 4.2.7 on 2023-11-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AddField(
            model_name='appealing',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='appealing',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='appealing',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='appealing',
            name='subject',
            field=models.CharField(max_length=255, null=True),
        ),
    ]