# Generated by Django 3.2.6 on 2021-09-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_profileclass_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='addclasswork',
            name='title',
            field=models.TextField(default='none', max_length=100),
        ),
    ]