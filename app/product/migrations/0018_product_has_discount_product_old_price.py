# Generated by Django 5.0 on 2024-01-12 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_comment_options_comment_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='əvvəlki qiymət'),
        ),
    ]
