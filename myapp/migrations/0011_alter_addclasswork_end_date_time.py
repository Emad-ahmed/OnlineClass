# Generated by Django 3.2.9 on 2021-11-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20211116_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addclasswork',
            name='end_date_time',
            field=models.DateTimeField(blank=True),
        ),
    ]