# Generated by Django 3.2 on 2021-12-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Warning'), (1, 'Published')], default=1),
        ),
    ]
