# Generated by Django 3.2.6 on 2021-08-21 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_addclasswork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinclass',
            name='createclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.createclass'),
        ),
    ]