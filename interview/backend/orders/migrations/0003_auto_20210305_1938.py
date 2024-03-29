# Generated by Django 3.1.7 on 2021-03-05 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20210305_1938'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='cart.cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
