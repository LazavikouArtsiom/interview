# Generated by Django 3.1.7 on 2021-03-06 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210305_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_with_sales',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]