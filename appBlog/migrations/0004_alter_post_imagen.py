# Generated by Django 4.1.3 on 2023-01-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0003_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(null='False', upload_to='posteos'),
        ),
    ]