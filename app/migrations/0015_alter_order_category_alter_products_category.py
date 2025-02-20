# Generated by Django 4.2 on 2024-07-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_order_category_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.CharField(choices=[('Cards', 'Cards'), ('Key Chain', 'Key Chain'), ('Mini', 'Mini'), ('Wood', 'Wood'), ('Accessories', 'Accessories'), ('Classic', 'Classic'), ('Phone Bag', 'Phone Bag')], max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Cards', 'Cards'), ('Key Chain', 'Key Chain'), ('Mini', 'Mini'), ('Wood', 'Wood'), ('Accessories', 'Accessories'), ('Classic', 'Classic'), ('Phone Bag', 'Phone Bag')], max_length=50),
        ),
    ]
