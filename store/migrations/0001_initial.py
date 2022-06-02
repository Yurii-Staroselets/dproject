# Generated by Django 4.0.5 on 2022-06-02 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorith',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algorith_or_models', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'algorith',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=245)),
                ('description', models.TextField(blank=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_6', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_7', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_8', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_9', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_10', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('slug', models.SlugField(max_length=245)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('algorith_or_models', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.algorith')),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='store.category'),
        ),
        migrations.AddField(
            model_name='algorith',
            name='brand_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='algorith', to='store.brand'),
        ),
        migrations.AddField(
            model_name='algorith',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='algorith', to='store.category'),
        ),
    ]